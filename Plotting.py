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

# Loosely based on https://gist.github.com/Overdrivr/efea3d363556c0dcf4b6

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from multiprocessing import Process,Pipe
import random
from GUI_colors import *

def Plot(link,N):

    colors = [active_blue_solid,active_blue,active_green,white,warning,
                critical, warning_solid]
    color  = colors[random.randint(0,len(colors)-1)] # unified color per plot

    pg.setConfigOption('background','#041a25')
    win = pg.GraphicsWindow()
    win.resize(600,400)
    win.setWindowTitle('Plot '+str(N))

    plots = {}
    data  = {}

    def add(name):
        plt_zone = win.addPlot(title = name)
        plt = plt_zone.plot(pen = color)
        plots[name] = plt
        data[name]  = []

    def update(link):
        communicate(link)
        if data:
            for name,plot in plots.items():
                plot.setData(data[name])

    def communicate(link):

        link.send('Rdy')
        try:
            received = link.recv()
        except EOFError as e:
            print('Plot.communicate exception >>',e)
            pass

        if 'new' in received:
            name = received.split(':')[1]
            add(name)

        elif type(received)==dict:
            for name,new_data in received.items():

                data[name].append(new_data)

                while len(data[name])>1000:
                    data[name].pop(0)

    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: update(link))
    timer.start(1)

    QtGui.QApplication.instance().exec_()
