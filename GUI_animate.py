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

from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation as QAnimate
from PyQt5.QtCore import QSequentialAnimationGroup as QSeqAnimate

def shake_animate(gui,shake_me):
      ''' Make the "shake_me" input object shake breifly '''
      start = QtCore.QPointF(shake_me.x(),shake_me.y())
      end   = QtCore.QPointF(shake_me.x()+5,shake_me.y())
      gui.animation_seq = QSeqAnimate()

      for n in range(5):
          animation = QAnimate(shake_me,b'pos')
          animation.setDuration(50)
          if n % 2 == 0:
              animation.setStartValue(end)
              animation.setEndValue  (start)
          else:
              animation.setStartValue(start)
              animation.setEndValue  (end)
          animation.setEasingCurve(QtCore.QEasingCurve.OutQuint)
          gui.animation_seq.addAnimation(animation)
      gui.animation_seq.start()
