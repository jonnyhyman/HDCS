"""
    This file is part of HDCS.

    HDCS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    HDCS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with HDCS.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import importlib
import Definitions
import Live_Keys

import numpy as np
import GUI_colors as colors

from time import time
from numpy.linalg import norm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from GUI_custom import plotDrop

from ADCS_Link import ADCS_Link
from GUI_accessories import Dialog, Sound
import Test_definition

""" ---------------------------------------------------------------------------
    Helper functions + variables
    ----------------------------------------------------------------------- """

def label_bounds(label): # convenience function to convert label to qgraphicsrect
    geo = label.geometry()
    return QtWidgets.QGraphicsRectItem(geo.x(),geo.y(),geo.width(),geo.height())

def extractCSS(style,att):
    beg   = style.index(att)+len(att)+1 # don't include :
    end   = style.index(';',beg) # don't include ';'
    return style[beg:end]

def changeCSS(label,style,attribute,target):
    style = style.replace(extractCSS(style,attribute),target)
    label.setStyleSheet(style)

# Direction Vectors, used to calculate optimal lines!

N = np.array([0, 1])
E = np.array([1, 0])
S = np.array([0, -1])
W = np.array([-1, 0])
NE = np.array([np.cos(np.pi/4), np.sin(np.pi/4)])
NW = np.array([3*np.cos(np.pi/4), np.sin(3*np.pi/4)])
SE = np.array([np.cos(-np.pi/4), np.sin(-np.pi/4)])
SW = np.array([np.cos(-3*np.pi/4), np.sin(-3*np.pi/4)])

directions = [NE, SE, SW, NW]

""" ---------------------------------------------------------------------------
    State label dynamic realtime updating functions
    ----------------------------------------------------------------------- """

def dub(data): # double printing scheme
    data ='{0:.02f}'.format(data)
    return str(data)

def trip(data): # triples printing scheme
    data ='{0:.03f}'.format(data)
    return str(data)

def alertState(gui,name):
    """ Get the alerting state, -1(OFF), 0(OK) , 1(WARNING), or 2(CRITICAL)
        For command blocks, returns the state of the object_name variable """

    state = gui.State[name]

    if name in gui.State_Limits_keys:

        lower = gui.State_Limits[name][0]
        upper = gui.State_Limits[name][1]

        if state >= upper:
            alert = 2
        elif state <= lower:
            alert = 2
        elif (state >= (upper-lower)*0.75+lower and state < upper):
            alert = 1
        elif (state <= (upper-lower)*0.25+lower and state > lower) :
            alert = 1
        elif state == -1:
            alert = -1 # not yet set
        elif (upper-lower)*0.25+lower < state < (upper-lower)*0.75+lower :
            alert = 0

    else:
        alert=state

    return alert, state

def colorBackState(alert,state):
    """ back color decider """
    if alert==state: # Command blocks will do this, nothing else
        if alert == 0:
            return QColor(colors.disabled)
        elif alert == 1:
            return QColor(colors.active_blue_solid)
    else:
        if alert == -1:
            return QColor(colors.disabled)
        elif alert == 0:
            return QColor(colors.active_blue_solid)
        elif alert == 1:
            return QColor(colors.warning_solid)
        elif alert == 2:
            return QColor(colors.critical)

def colorFloatingBackState(alert,state):
    """ back color decider for "floating" blocks (text state colorers) """
    if alert==state: # Command blocks will do this, or disabled sensors
        if alert == 0:
            return QColor(colors.white)
        elif alert == 1:
            return QColor(colors.white)
        elif alert == -1:
            return QColor(colors.transparent)
    else:
        if alert == -1:
            return QColor(colors.transparent)
        elif alert == 0:
            return QColor(colors.transparent)
        elif alert == 1:
            return QColor(colors.transparent)
        elif alert == 2:
            return QColor(colors.white)

def colorForeState(alert,state):
    """ fore color decider """
    if alert==state: # Command blocks will do this, or disabled sensors
        if alert == 0:
            return QColor(colors.disabled)
        elif alert == 1:
            return QColor(colors.active_blue_solid)
        elif alert == -1:
            return QColor(colors.disabled)
    else:
        if alert == -1:
            return QColor(colors.disabled)
        elif alert == 0:
            return QColor(colors.active_green)
        elif alert == 1:
            return QColor(colors.warning_solid)
        elif alert == 2:
            return QColor(colors.critical)

def updateLabel(gui,name):
    """ Update a specific state label in Interface.stateLabels
        All calls are try/except wrapped to prevent needless crashes
    """

    flag, fg, bg = gui.stateLabels[name] # flag, foreground, background

    alert, value = alertState(gui,name) # value is Interface.State[name]

    if 'cs' in flag: # text colors state
        if 'd1' in flag: # text displays state

            fg.setText(dub(value))
            rebrush = fg.brush()
            try: # TEMP
                rebrush.setColor( colorForeState(alert,value) )
            except:
                print(name)
            fg.setBrush(rebrush)

            rebrush = bg.brush()
            rebrush.setColor( colorFloatingBackState(alert,value) )
            bg.setBrush(rebrush)

        elif 'd0' in flag: # text does not display state

            rebrush = fg.brush()
            rebrush.setColor( colorForeState(alert,value) )
            fg.setBrush(rebrush)

            rebrush = bg.brush()
            rebrush.setColor( colorFloatingBackState(alert,value) )
            bg.setBrush(rebrush)

    elif 'bs' in flag: # back colors state
        if 'd1' in flag:

            fg.setText(dub(value))
            rebrush = bg.brush()

            try:
                rebrush.setColor( colorBackState(alert,value) )
                bg.setBrush(rebrush)
            except TypeError: # Occurs for objects need manual coloring
                pass

        elif 'd0' in flag:

            rebrush = bg.brush()
            rebrush.setColor( colorBackState(alert,value) )
            bg.setBrush(rebrush)

""" ---------------------------------------------------------------------------
    Dynamic line creation and updating
    ----------------------------------------------------------------------- """

def makeLine(gui,p1,p2,scene,view):
    ''' Make a nicely bent line between the nodes '''

    # Check if y position is 'pretty much' equal
    if abs(p1.y()-p2.y()) < p1.height()/2:
        y_similar = 1
    else:
        y_similar = 0

    # Check if x position is 'pretty much' equal
    if abs(p1.x()-p2.x()) < p1.width()/2:
        x_similar = 1
    else:
        x_similar = 0

    # If aligned in at least one axis
    if ((x_similar and y_similar) or (x_similar and not y_similar)
                                  or (not x_similar and y_similar) ):

        r1 = [p1.x() + p1.width()/2,p1.y() + p1.height()/2]
        r2 = [p2.x() + p2.width()/2,p2.y() + p2.height()/2]

        r1 = view.mapFromScene(r1[0],r1[1])
        r2 = view.mapFromScene(r2[0],r2[1])

        line   = QtCore.QLineF(r1,r2)
        pen    = QtGui.QPen(QtGui.QColor(colors.disabled))

        linerefs = [scene.addLine(line,pen)]
        #pens     = [pen]

    else: # If not aligned in any axis

        # Create vector between points
        r1 = [p1.x() + p1.width()/2,p1.y() + p1.height()/2]
        r2 = [p2.x() + p2.width()/2,p2.y() + p2.height()/2]
        shortest = np.array(r2)-np.array(r1)

        # Find which direction vector (N, NE, E, etc.) is closest to the vector

        angles = []
        for vector in directions:
            vector = np.array(vector)
            dotnorm = np.dot(vector,shortest)
            dotnorm = dotnorm / np.dot(norm(vector),norm(shortest))
            angles.append(np.arccos(dotnorm))

        i = angles.index(min(angles))

        # Create a line with the vector's direction, multiplied by a magnitude
        # which puts either x or y smack-dab aligned with point 2

        mea = list(abs(shortest)).index(min(abs(shortest))) # min error axis
        mag = abs(shortest)[mea]/abs(directions[i][mea])

        vect = mag*directions[i] #*(norm(shortest)/np.cos(angles[i]))

        vect[0]+=r1[0]
        vect[1]+=r1[1]

        r1  = view.mapFromScene(r1[0],r1[1])
        mid = view.mapFromScene(vect[0],vect[1])

        line   = QtCore.QLineF(r1,mid)
        pen    = QtGui.QPen(QtGui.QColor(colors.disabled))

        linerefs = [scene.addLine(line,pen)]

        r2 = view.mapFromScene(r2[0],r2[1])

        line   = QtCore.QLineF(mid,r2)
        pen    = QtGui.QPen(QtGui.QColor(colors.disabled))

        lineref = scene.addLine(line,pen)

        linerefs.append( lineref )

    return linerefs

def makeLines(gui,scene,view):
    """ Make nicely bent lines between all qualified nodes """
    start = time()

    All = gui.centralwidget.findChildren(QtWidgets.QLabel)
    Labels = {obj.objectName(): obj for obj in All}

    p1 = gui.adcs_u1.geometry()
    p2 = gui.u1_adcs.geometry()

    # Create all labels, in both directions
    lines = {}
    for name,obj in Labels.items():
        pair = {}
        for other_name in Labels.keys():
            namecmp = name.split('_')
            othncmp = other_name.split('_')
            if ( set(namecmp).issubset(set(othncmp)) and (name!=other_name)
            and ('_' in name) and ('label' not in name)):
                pair[name]=other_name

        if len(pair)>0:
            for key,match in pair.items():
                p1 = Labels[key].geometry()
                p2 = Labels[match].geometry()
                lines[name] = makeLine(gui, p1, p2, scene, view)

    # Take duplicate lines, and decide which is the best,
    # then delete the one that isn't as good.

    lines_mod = dict(lines)
    for name,line in lines.items():

        line_pair = None
        for other_name in Labels.keys():
            namecmp = name.split('_')
            othncmp = other_name.split('_')
            if ( set(namecmp).issubset(set(othncmp)) and (name!=other_name)
            and ('_' in name) and ('label' not in name) ):

                line_pair=(lines[name],lines[other_name]) # found a pair, yay!
                break

        if len(line_pair) > 1:

            line_items = line_pair[0] # [primary line]
            othr_items = line_pair[1] # [other line]

            cost_line, cost_othr = 0.0, 0.0 # cost variables

            # Count collisions with any other labels, add that to the cost
            # Takes about 0.1s

            for _, label in Labels.items():
                for segment in line_items:
                    cost_line += float(segment.collidesWithItem(label_bounds(label)))
                for segment in othr_items:
                    cost_othr += float(segment.collidesWithItem(label_bounds(label)))

            # Add up length of line segments, add that to the cost

            for segment in line_items:
                cost_line += segment.shape().length()
            for segment in othr_items:
                cost_othr += segment.shape().length()

            # Just in case lengths + # collisions is identical,
            # also add to cost the float proximity to other labels,
            # but not including the endpoints! (too much proximity there)
            # -> Note the weight meaning we don't value this as much

            for _, label in Labels.items():
                segment = line_items[0] # [1st segment]
                label_ctr = label_bounds(label).boundingRect().center()
                cost_line += 1/(0.1+(segment.line().p2()-label_ctr).manhattanLength())

                segment = othr_items[0] # [1st segment]
                label_ctr = label_bounds(label).boundingRect().center()
                cost_othr += 1/(0.1+(segment.line().p2()-label_ctr).manhattanLength())


            # Figure out who is worse, and mark for deletion

            if cost_line > cost_othr:
                deleteme = [name,line_pair[0]]
            else:
                deleteme = [other_name,line_pair[1]]

            try:
                #print('del',deleteme[0])
                lines_mod.pop(deleteme[0]) # remove by key, deletes lines + pens
                for segment in deleteme[1]:
                    scene.removeItem(segment) # remove line objects in scene

            except KeyError as e: # happens if line was deleted earlier and we missed it
                pass

    lines = lines_mod
    gui.line_keys = lines.keys()

    print('Line generation took',time()-start,'seconds')

    return lines

def updateLineStates(gui,line_name):
    """ update a single line's state, inherited from its connected nodes """

    # first, make some decisions based on the line's name

    node_names = line_name.split('_')

    if ( (node_names[0] in Definitions.Control_Keys) and
    (node_names[1] in Definitions.Control_Keys) ):

         # Hey, that means this is a COMMAND line!
         # (Both ends must be active for the line to activate)

        if gui.State[node_names[0]] and gui.State[node_names[1]]:
            # Turn on!
            for segment in gui.lines[line_name]:
                repen = segment.pen()
                repen.setColor( QColor(colors.active_blue_solid) )
                segment.setPen( repen )
        else:
            # Turn off
            for segment in gui.lines[line_name]:
                repen = segment.pen()
                repen.setColor( QColor(colors.disabled) )
                segment.setPen( repen )

    else:

        # Hey, that means this is a NON-COMMAND line!
        # (Only one end must be active for the line to activate)

        # Pick the end that actually IS in gui.State
        for name in node_names:
            if name in gui.stateLabel_keys:
                name = name
                break

        # Turn on/off - with the same color!
        flag, fg, bg = gui.stateLabels[name] # flag, foreground, background

        alert, value = alertState(gui,name) # value is Interface.State[name]

        if 'cs' in flag:
            buddybrush = fg.brush()
        elif 'bs' in flag:
            buddybrush = bg.brush()

        buddycolor = buddybrush.color()
        for segment in gui.lines[line_name]:

            repen = segment.pen()
            repen.setColor( buddycolor )
            repen.setWidth( alert+1 ) # range from 1-3 in width
            segment.setPen( repen )

""" ---------------------------------------------------------------------------
    Functions to update specific elements of the gui not encompassed by dynamic
    lables or dynamic lines
    ----------------------------------------------------------------------- """

def updateThrust(gui):

    """ Update the thrust direction plot """

    xy = np.array([ gui.State['z0']-gui.State['z2'],
                    gui.State['z1']-gui.State['z3'] ])

    if norm(xy) > 77:
        xy = 77*xy/norm(xy)

    centerx=gui.xyfbg.x()+gui.xyfbg.width()/2
    centery=gui.xyfbg.y()+gui.xyfbg.height()/2
    center = QtCore.QPointF(centerx, centery)

    xy     = QtCore.QPointF(centerx+xy[0], centery+xy[1])
    line   = QtCore.QLineF(center,xy)
    pen    = QtGui.QPen(QtGui.QColor(colors.active_blue))
    pen.setWidthF(3)

    if hasattr(gui,'xyflineref'):
        gui.xyflineref.setLine(line)
    else:
        gui.xyflineref = gui.scene.addLine(line,pen)

def updateLiveLog_Keys(gui):

    try:
        importlib.reload(Live_Keys)
    except:
        pass

    gui.livelog_keys = Live_Keys.keys

    for key in list(Live_Keys.keys):
        if key not in Definitions.State:
            gui.livelog_keys.remove(key)

def updateLiveLog(gui,init=False):

    if init:
        gui.live_log_frozen = 1
        gui.livelog_freeze_button.setChecked(1)

    if not gui.live_log_frozen:
        gui.livelog.setTextColor(QtGui.QColor('#FFFFFF'))

        updateLiveLog_Keys(gui)

        line = ''.join([' %s:%s |' % (key, gui.State[key])
                        for key in gui.livelog_keys])

        gui.livelog.insertPlainText(line+'\n')
        gui.livelog.moveCursor(QtGui.QTextCursor.End)


def updateRegulator(gui):

    """ Update the regulator view """

    r = gui.State['Rn']
    gui.Rnum.setText(dub(r))
    geo =  QtCore.QRect(453,420,71*r,41)
    geo = gui.Rnumbar.setGeometry(geo)

def updateAnnunciator(gui,init=False):
    """ Update or initialize the annunciator panel """

    if init:
        gui.flames.setVisible(0)
        gui.CSYNC.setVisible(0)
        gui.fa1.setVisible(0)
        gui.fa2.setVisible(0)

    else: # general update takes no arguments

        gui.fa1.setVisible(gui.State['Fa1'])
        gui.fa2.setVisible(gui.State['Fa2'])
        gui.u3disconn.setVisible(not gui.State['u3'])
        gui.u4disconn.setVisible(not gui.State['u4'])
        gui.pwrdisconn.setVisible(not (gui.State['B1'] and gui.State['B1']) )
        gui.CSYNC.setVisible((gui.State['C1'] - gui.State['C2']
                                    >= gui.State_Limits['C1-2'][1]))

        if gui.State['A'] and gui.State['B'] and gui.State['Rbool']:
            gui.flames.setVisible(1)
        else:
            gui.flames.setVisible(0)

        gui.stop_state.setVisible(gui.State['E'])
        gui.arm_state.setVisible(gui.State['a'])

        if gui.l_State['F1'] != gui.State['F1']:
            gui.f1_toggle()

        if gui.l_State['F2'] != gui.State['F2']:
            gui.f2_toggle()

def updateAlarms(gui):
    """ Update the master caution and warning alarms + sounds"""

    # Perform state checks at time interval

    warning_keys = [('E',1),]

    for warning_key, sensitivity in warning_keys:
        if gui.State[warning_key] == sensitivity:
            if gui.State[warning_key] != gui.l_State[warning_key]:
                gui.Alarms['warning'].append((warning_key,sensitivity))

    caution_keys = [('u3',0),('u4',0),('B1',0),('B2',0),('a',0)]

    for caution_key, sensitivity in caution_keys:
        if gui.State[caution_key] == sensitivity:
            if gui.State[caution_key] != gui.l_State[caution_key]:
                gui.Alarms['caution'].append((caution_key,sensitivity))

    # Perform alarm updates

    if len(gui.Alarms['warning']):

        gui.sound('caution')
        gui.warning_alarm.setStyleSheet(''' color: white;
                                            background-color:#B02109;
                                            border: 1px solid white;''')

        # for all active, double check if needs to be

        for warning_key, sensitivity in gui.Alarms['warning']:
            if gui.State[warning_key] != sensitivity:
                gui.Alarms['warning'].remove((warning_key,sensitivity))
                if len(gui.Alarms['warning']) == 0:
                    gui.warning_alarm.setStyleSheet('''color: gray;
                                                       background-color:transparent;
                                                       border: 1px solid gray;''')

    elif gui.Alarms['warning'] != gui.l_Alarms['warning']:

        gui.warning_alarm.setStyleSheet(''' color: gray;
                                            background-color:transparent;
                                            border: 1px solid gray;''')

    if len(gui.Alarms['caution']):

        # Space time intervals farther
        if time() - gui.l_Caution >= 1:
            gui.l_Caution = time()
            gui.sound('caution')

        gui.caution_alarm.setStyleSheet(''' color: white;
                                            background-color:#dd6300;
                                            border: 1px solid white;''')

        for caution_key, sensitivity in gui.Alarms['caution']:
            if gui.State[caution_key] != sensitivity:
                gui.Alarms['caution'].remove((caution_key,sensitivity))
                if len(gui.Alarms['caution']) == 0:
                    gui.caution_alarm.setStyleSheet('''color: gray;
                                                       background-color:transparent;
                                                       border: 1px solid gray;''')

    elif gui.Alarms['caution'] != gui.l_Alarms['caution']:
        gui.caution_alarm.setStyleSheet(''' color: gray;
                                            background-color:transparent;
                                            border: 1px solid gray;''')

def updateCount(gui):

    flag, fg, bg = gui.stateLabels['count']

    if gui.State['Cm']==0:
        if gui.State['C1']>=-10: # inside 10 sec, critical if halted
            alert = 2
        else:
            alert = -1
    elif gui.State['Cm']==1:
        alert = 0
    elif gui.State['Cm']==2:
        alert = 1

    rebrush = bg.brush()
    rebrush.setColor( colorBackState(alert,10) ) # 10 makes color mode as we want
    bg.setBrush(rebrush)

def updateComms(gui):
    # to prevent colors from looking disconnected when dt==0.0, add tiny amount
    gui.State['dt'] = time() - gui._Thread.lasttime + 0.0000001
    updateLabel(gui,'dt')

    if gui._Thread.ADCS.connected:
        gui.State['adcs'] = 1
        gui.State['hdcs'] = 1
        gui.setWindowTitle("Human Digital Control Station [HDCS] - Connected")
    else:
        gui.State['adcs'] = 0
        gui.State['hdcs'] = 0
        gui.setWindowTitle("Human Digital Control Station [HDCS] - Disconnected")

    updateLabel(gui,'adcs')

    line_key = gui.look_for_linekey('adcs','it')
    updateLineStates(gui,line_key)

def updateCommands(gui):
    """ Update any Commands which need to be reset or verified,
        or act on Commands which have evolved into States """

    # Update wireless control link(s)
    gui.Command_F2.update(gui,['F2'])

    if gui.Command['UC']:
        # If had sent an upload command, reset to prevent re-requesting
        gui.Command['UC']=0

    if gui.Command['RS']=='MICRO':
        # If had sent a micro reset, reset to prevent re-requesting
        gui.Command['RS']=0

    if gui.Command['RS'] == 'ADCS' and not gui._Thread.ADCS.connected:
        # If had sent an ADCS reset, and we observe disconnect, clear the cmd
        gui.Command['RS']=0

    if gui.Command['RS'] == 'ADCS_OFF' and not gui._Thread.ADCS.connected:
        # If had sent an ADCS stop, and we observe disconnect, clear the cmd
        gui.Command['RS']=0

    if gui.State['TM']:
        # Upload the matrix one line at a time, one transaction at a time
        if gui.State['TM'] > len(gui.tdf.TestMatrix):
            gui.Command['TM'] = 0
        else:
            try:
                gui.Command['TM'] = gui.tdf.TestMatrix[gui.State['TM'] - 1]
                print('>>TM STATE',gui.State['TM'],'OBSERVED, COMMANDING:',gui.Command['TM'])
            except IndexError as e:
                print("updateCommands for 'TM' exception >>",e)

    # Back-propogate feedback command states to command variable
    '''
    for key in Definitions.Feedback_Command_Keys:
        if (gui.Command[key] != gui.State[key] and
            gui.l_Cmd[key] != gui.l_State[key] ) :

            # If TWICE the state was not the command,
            # we have a back-propogated switch event

            gui.Command[key] = gui.State[key]
    '''

def updateAverages(gui,keys):
    for key in keys:

        try:
            gui.averages[key]['vals'].append(gui.State[key])
        except KeyError:
            # first time
            gui.averages[key] = {}
            gui.averages[key]['vals'] = [gui.State[key]]

        if len(gui.averages[key]['vals']) > 10:
            gui.averages[key]['vals'].pop(0)

        history = gui.averages[key]['vals']

        gui.averages[key]['avg'] = sum(history) / len(history)

def updateGenerated(gui):
    """ Update state variables which are generated from other data """

    # Regulator variables
    gui.State['Rbool'] = int(bool(gui.State['R']))
    gui.State['Rn']    = gui.State['R']/100

    # Thrust variables
    gui.State['xf0'] = gui.State['z0']+gui.State['z1']
    gui.State['xf1'] = gui.State['z2']+gui.State['z3']
    gui.State['yf0'] = gui.State['z1']+gui.State['z2']
    gui.State['yf1'] = gui.State['z0']+gui.State['z3']
    gui.State['zf'] = (gui.State['z0']+gui.State['z1']+
                       gui.State['z2']+gui.State['z3'])

    # Count variable
    gui.State['count']  = (gui.State['c1']+gui.State['c1_']/1000)
    gui.State['count'] += (gui.State['c2']+gui.State['c2_']/1000)
    gui.State['count'] /= 2

    # Latest non-zero mass flow rate
    if abs(gui.State['m0'] - gui.State['l_m0']) > 0:
        gui.State['dm0']   = (gui.State['m0'] - gui.State['l_m0'])
        gui.State['dm0']  /= (time() - gui.last_m0_check)
        gui.last_m0_check  = time()

    gui.State['l_m0']  = float(gui.State['m0'])

    # Average variables
    updateAverages(gui,['m0','zf','t1','t2'])

def addPlot(gui):

    """ Add a new plot to the program """

    gui.beingDragged = []

    if len(gui.plots)<=7: # >7 exceeds width of over-cover

        plot = plotDrop(gui,len(gui.plots),gui.plotDropFrame)

        gui.scene.addItem(plot)
        gui.plots += [plot]

        print('Added plot!')

def freezePlots(gui,value):
    for plot in gui.plots:
        plot.freeze(value)

def closePlots(gui):

    """ Close all plots currently active """

    for plot in gui.plots:
        plot.remove()
        gui.scene.removeItem(plot)

    gui.plots = []

""" ---------------------------------------------------------------------------
    Updating for all state variable views
    ----------------------------------------------------------------------- """

def updateState(gui,state):

    #start = time()

    gui.State.update(state)

    # These must be run before others
    updateCount(gui)
    updateComms(gui)
    updateCommands(gui)
    updateGenerated(gui)

    # Update master alarms
    updateAlarms(gui)

    # Update plot windows
    for plot in gui.plots:
        plot.update(gui.State)

    # Update state labels
    for name in gui.stateLabel_keys:
        updateLabel(gui,name)

    # Update dynamic line states
    for line_name in gui.line_keys:
        updateLineStates(gui,line_name)

    # Update other elements

    updateThrust(gui)
    updateLiveLog(gui)
    updateRegulator(gui)
    updateAnnunciator(gui)
    gui.procs.autoChecks()

    # Save copy of last state and command
    gui.l_State = dict(gui.State)
    gui.l_Cmd   = dict(gui.Command)
    gui.l_Alarms = dict(gui.Alarms)

    if gui.log.active:
        gui.log.Commit([gui.State,gui.Command])

    #print('Update:',1/(time()-start),'Hz')
