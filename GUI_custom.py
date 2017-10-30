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

import Plotting as plot
import GUI_colors as colors
from PyQt5 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg
from multiprocessing import Process,Pipe

class plotDrop(QtWidgets.QGraphicsEllipseItem):
    def __init__(self,gui,N,Frame):

        """ Plot drop holds the circle objects which act as drop zones for
            variables to plot.

            Also, plot drop instantiates and provides minimal controls for its
            specifically owned plot windows.
        """

        self.gui = gui
        self.N   = N

        spacing = 10

        w   = 71
        h   = 71
        x   = Frame.x() + N*w + N*spacing
        y   = Frame.y()

        super(self.__class__, self).__init__(x,y,w,h)

        pen   = QtGui.QPen(QtGui.QColor(colors.disabled_lite))
        font  = QtGui.QFont()

        font.setFamily("GOST Common")
        font.setPointSize(14)
        fbrush = QtGui.QBrush( QtGui.QColor(colors.disabled_lite),
                               QtCore.Qt.SolidPattern )

        pen.setStyle(QtCore.Qt.DashLine)
        self.setPen(pen)
        self.setAcceptHoverEvents(True)

        self.number = QtGui.QGraphicsSimpleTextItem(str(N),self)
        self.number.setFont(font)
        self.number.setBrush(fbrush)
        self.number.setX(x+w/2.3)
        self.number.setY(y+h/3.5)

        self.gui.scene.addItem(self.number)
        self.plots = []

        self.data_freeze = 0

        self.a,b = Pipe()
        self.p = Process(target=plot.Plot, args=(b,self.N,))
        self.p.start()

    def add(self,name):
        print('Adding',name,'to plot',self.N)
        self.a.send('new:'+name)
        self.plots.append(name)

    def update(self,state):
        """ Update plots with new state """

        up_state = {}
        if not self.data_freeze:
            for plot_var in self.plots:
                up_state[plot_var] = state[plot_var]

        if self.p.is_alive():
            if self.a.poll():
                self.a.recv()
                self.a.send(up_state)
        else:
            self.gui.closeSpecificPlot(self)

    def freeze(self,value):
        self.data_freeze = value

    def hoverEnterEvent(self,event):

        """ In PyQt5, Python3.6, drag and drop appears to be broken for
            QGraphicsEllipseItem's. So, we hack the hoverEnterEvent to
            do drag and drop """

        if len(self.gui.beingDragged)>0:
            self.add(self.gui.beingDragged)

    def remove(self):
        """ Delete the child """
        if self.p.is_alive():
            self.p.terminate()
        self.gui.scene.removeItem(self.number)

class labelHandle(QtWidgets.QGraphicsRectItem):
    def __init__(self,gui,rect,pen,brush):

        """ Provide a "cloned" label to stay in the place of a display blocks
            while the display block is being dragged into a plot zone """

        super(self.__class__, self).__init__(rect)
        self.gui = gui
        self.setPen(pen)
        self.setBrush(brush)
        self.setOpacity(0.5)

class labelRect(QtWidgets.QGraphicsRectItem):
    def __init__(self,gui,name,x,y,w,h,pen,brush):
        """ Graphics item class for all state labels """

        super(self.__class__, self).__init__(x,y,w,h)
        self.name = name
        self.gui  = gui
        self.setPen(pen)
        self.setBrush(brush)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
        self.default_pos = self.pos()

    def mousePressEvent(self, event):
        """ Initiate the drag into a plot zone """
        self.clone_label = labelHandle(self.gui,self.rect(), self.pen(), self.brush())
        self.gui.scene.addItem(self.clone_label)
        self.gui.beingDragged = self.name

        self.gui.plotDropFrame.setVisible(0) # Reveal the plot circles

    def mouseReleaseEvent(self, event):
        """ Complete the drag into a plot zone """

        self.gui.scene
        self.gui.scene.removeItem(self.clone_label)
        del self.clone_label # delete my double, I'm goin' home!!

        self.setPos(self.default_pos) # to the plaaaaace - where I belong!!
        self.setSelected(0)

        self.gui.plotDropFrame.setVisible(1) # Cover up the circles
