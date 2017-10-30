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

import os
import types
from time import time
from pprint import pprint
from Definitions import *
ln='\n'

def def_logging(matrix,defined,notes):
    """ Log all aspects of the test definition, for later retrieval and
        association with test data. Saves as a pure python file
    """

    logno=0
    while (os.path.isfile('./logs/'+"log_"+str(logno)+".csv")):
        logno+=1

    with open('./logs/'+"def_"+str(logno)+".py", "w") as log_file:

        # Replace regulator with function name, not pointer, if necessary:
        if callable(defined['R_pos']):
            defined['R_pos'] = defined['R_pos'].__name__

        log_file.write( """ # Test Definition for Log File """+str(logno) )

        log_file.write('''\nTestNotes =""" ''')

        pprint( (notes) , stream = log_file )

        log_file.write(''' """\n''')

        log_file.write("""TestParams = """)

        pprint( (defined) , stream = log_file )

        log_file.write( (ln+"""TestMatrix = """) )

        pprint( (matrix) , stream = log_file )

        regScript = open('RegulatorScript.py','r')

        log_file.write( (regScript.read()) )

class Log(object):
    def __init__(self,data_dicts):
        """ This class operates extremely fast data logging to disk.

            - To be extremely fast, we hold the file pointer until we
              are completely done, at which point we close.

            - We also make use of join method rather than concatenate, and
              only perform 1 write per commit

        """

        self.data_dicts = data_dicts # take a list of pointers to data dicts
        self.active = 0

    def begin(self):

        self.start  = time()
        self.active = 1

        logno=0
        while (os.path.isfile('./logs/'+"log_"+str(logno)+".csv")):
            logno+=1

        self.file = open('./logs/'+"log_"+str(logno)+".csv",'a')

        join_list = ['T'] # Time always goes first!

        for data in self.data_dicts: # Get keys in each data_dict
            join_list.extend([',%s' % key for key in sorted(data)])

        join_list.extend(['\n'])

        self.file.write(''.join(join_list))

    def Commit(self,data_dicts):
        """ Commit the current data dictionaries to file """

        join_list = [str(time()-self.start)] # Time always goes first!

        for data in data_dicts: # Get data in each data_dict
            join_list.extend([',%s' % data[key] for key in sorted(data)])

        join_list.extend(['\n'])

        self.file.write(''.join(join_list))

    def stop(self):
        """ Close the log file """

        self.file.close()
        self.active = 0

if __name__ == '__main__':

    dict1 = {'A':1,'B':2,'C':3.5}
    dict2 = {'D':4,'E':5,'F':1241.00}
    dictionaries = [dict1,dict2]
    log = Log(dictionaries)

    start =time()
    log.Commit()
    print(time()-start)
    log.close()
