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

from multiprocessing import Process,Pipe
from time import time, sleep
import socket
import ast

class Wireless_Control(object):
    def __init__(self,ip,port):
        """ Finds the wireless controller's IP by its mac address + connects """

        self.UDP_IP   = ip
        self.UDP_PORT = port

        self.controller, self.link = Pipe()
        self.comm_prc = Process(target=self.controller_check,args=(self.link,))
        self.comm_prc.daemon = True # quit when main quits
        self.comm_prc.start()

        self.last_filtered_commands = {}

    def controller_check(self,link):
        """ Connect to controller and parse its data """

        sock = socket.socket(socket.AF_INET,    # Internet
                             socket.SOCK_DGRAM) # UDP

        while True:

            sock.settimeout(0.5)
            send_cmd = link.recv()

            send_cmd = ''.join(['%s:%s,' % (key,value)
                                for key,value in send_cmd.items()])

            try:
                sock.sendto(bytes(str(send_cmd),'utf-8'), (self.UDP_IP, self.UDP_PORT))
            except socket.timeout:
                pass

            try:
                data,addr = sock.recvfrom(1024)
                if data:
                    data = data.decode('utf-8')
                    data = data.replace("F2"," 'F2' ")
                    data = ''.join( ['{',data,'}'] )
                    data = ast.literal_eval(data) # make into actual dictionary
                    link.send(data)

            except socket.timeout:
                pass

    def update(self,gui,filter_keys):
        """ Transceive from the controller_check process pipe; update state"""

        filtered_cmds = { key : gui.Command[key] for key in filter_keys }

        # only send on command CHANGEs, to allow multiple controllers
        if filtered_cmds != self.last_filtered_commands:
            self.controller.send(filtered_cmds)

        self.last_filtered_commands = dict(filtered_cmds)

        if self.controller.poll():
            data = self.controller.recv()
            if data:
                try:
                    gui.State['F2'] = data['F2']

                except KeyError:
                    pass # partial data will cause this

    def close(self):
        self.comm_prc.terminate()


if __name__ == '__main__':

    F2_link  = Wireless_Control(ip="192.168.11.125",port=18015)

    state = {'F2':0}
    cmd   = {'F2':1}

    while True:
        sleep(0.1)
        F2_link.update(state,cmd)
        print('State:',state)
