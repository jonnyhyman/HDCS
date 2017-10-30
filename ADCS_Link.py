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

import socket
import sys
from time import time
import ast
import Definitions

class ADCS_Link(object):
    def __init__(self):
        """ Create a TCP/IP socket, and connect """
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.settimeout(1)

        self.last_cmd = dict(Definitions.Command)
        self.last_newCmds = {}

        print('Attempting TCP connect...')

        self.n = 0
        self.host  = 'adcs.local'
        self.connected = False
        self.ports = [50010,50020,50030]

        self.tcp_connect()

    def tcp_connect_core(self,host,port):

        self.tcp_server_addr = (host, port)

        try:
            self.tcp.connect(self.tcp_server_addr)
            self.connected = True
            print('tcp AOS!',self.tcp_server_addr)
            return True

        except socket.timeout:
            return False

        except Exception as e:
            print('ADCS_Link.tcp_connect_core, exception:',e)
            return False


    def tcp_connect(self):
        """ Connect the socket to the port where the server is listening """

        try:
            self.port = self.ports[self.n]
        except IndexError:
            self.n = 0 # for the button spammers out there
            self.port = self.ports[self.n]

        if not self.tcp_connect_core(self.host,self.port):
            self.n += 1
            print('ADCS_Link.tcp_connect, Port',self.port,'no connection')
        else:
            if not self.transcieve(self.last_cmd,{}):
                # Blocks connection w/the wrong port
                print('ADCS_Link.tcp_connect, Port',self.port,'no response')
                self.n += 1
                self.connected = False
            else:
                print('ADCS_Link.tcp_connect, Port',self.port,'got response!')

        if self.n >= len(self.ports):
            self.n=0

    def persistence_check(self,cmd,state):

        self.persist_cmds = {}
        self.cmd = cmd
        self.state = state

        for key in [key for key in cmd if key in Definitions.Persist_Criteria]:
            if key in self.last_newCmds:
                for criterion in Definitions.Persist_Criteria[key]:
                    try:
                        if not eval(criterion):
                            self.persist_cmds[key] = cmd[key]
                            break
                    except Exception as e: # eval can cause errors
                        print('ADCS_Link.persistence_check exception >>',e)
                        pass


    def send(self,cmd,state):
        """ Send command update string to socket """
        try:

            # Build the list of commands which should persist
            self.persistence_check(cmd, state)

            # Build new and persistent commands dictionary
            newCmds = { key:value for key,value in cmd.items()
                         if (cmd[key] != self.last_cmd[key]
                             or  key  in self.persist_cmds   ) }

            if newCmds!={}:
                self.tcp.sendall(bytes(str(newCmds),'utf-8'))
                self.last_cmd = dict(cmd)

            self.last_newCmds = dict(newCmds)

        except (ConnectionResetError,socket.timeout,OSError) as e:
            #print('tcp send error',e)
            self.connected = False


    def receive(self):
        """ Receive state string from socket """
        try:
            return self.tcp.recv(4096)
        except socket.timeout:
            #print('tcp recv timeout')
            #self.connected = False
            return None
        except (ConnectionResetError,OSError) as e:
            #print('tcp recv error',e)
            self.connected = False
            return None


    def transcieve(self,cmd,state):
        """ Send + Receive from the TCP socket, or time out """
        self.send(cmd,state)
        return self.receive()

    def state_parser(self,data):
        """ Parse the latest received state data string into a dict """

        data = data.decode()

        # The TCP data has old data mixed in, so be sure to only get the latest
        start,end = data.rfind('{'), data.rfind('}')+1 # INCLUDE BRACES

        if start>=end:
            #If TCP got only string with } BEFORE {, then EOF will occur
            # Get the actual start, BEFORE the last }
            start = data.rfind('{',0,end)

        new_data  = data[start:end]

        try:
            return ast.literal_eval(new_data)
        except:
            pass

    def tranceive_and_parse(self,cmd,state):
        """ Do both receiving and parsing, and return the new state """
        if self.connected:

            data = self.transcieve(cmd,state)
            if data is not None:
                return self.state_parser(data)

        else:
            self.reconnect()

    def reconnect(self):
        """ Close socket, create anew, attempt connect """
        self.close()
        print('ADCS_Link.reconnect, close complete')
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.settimeout(1)
        print('ADCS_Link.reconnect, socket reset complete')
        self.tcp_connect()
        print('ADCS_Link.reconnect, tcp connect complete')

    def close(self):
        self.tcp.close()

if __name__ == '__main__':
    ADCS = ADCS_Link()
    while True:
        state = ADCS.tranceive_and_parse(Definitions.Command) # None if nothing received
        if state:
            print('Received',len(state),'key long state')
