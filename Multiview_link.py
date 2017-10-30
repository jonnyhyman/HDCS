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

from socket import *
from time import *

def dub(data): # double printing scheme
    data ='{0:.02f}'.format(data)
    return data

class Multiview_Link(object):

    def __init__(self):
        self.tx = socket(AF_INET, SOCK_DGRAM)
        self.txAddr_S = ('', 13000)
        self.tx.bind(self.txAddr_S)
        self.tx.settimeout(0.01)
        self.tx.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def reopen(self):
        self.tx = socket(AF_INET, SOCK_DGRAM)
        self.txAddr_S = ('', 13000)
        self.tx.bind(self.txAddr_S)
        self.tx.settimeout(0.01)
        self.tx.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def close(self):
        self.tx.close()

    def Send(self,state):
        data=0
        try:
            data, self.server = self.tx.recvfrom(16) # 16 bytes MAX (trigger only)
        except:
            pass

        if data:
            ToView=''
            ToView+='CD:'+dub(state['C']+state['C_']/1000)+','
            ToView+='Cm:'+str(state['Cm'])+','

            ToView+='ZS:'+dub(state['z0'] + state['z1']+
                              state['z2'] + state['z3'])+','

            ToView+='t1:'+dub(state['t1'])+','
            ToView+='t2:'+dub(state['t2'])+','

            ToView = ToView.replace(',,',',') # garbage collection :)

            #print('SENDING VIEWER -->',ToView)
            self.tx.sendto(bytes(ToView,'utf-8'),self.server)
            self.ltx = time()
