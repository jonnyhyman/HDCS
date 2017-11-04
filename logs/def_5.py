 # Test Definition for Log File 5
TestNotes =""" 'HOT FIRE 1 : ATTEMPT 2 : PYRO IGNITION'
 """
TestParams = {'A_del': 0.0,
 'A_dur': 2.0,
 'B_del': 0.0,
 'B_dur': 2.0,
 'I_del': 0.0,
 'I_dur': 0.2,
 'R_dur': 2.0,
 'R_pos': 'Regulator',
 'tminus': 420.0}

TestMatrix = [[-420.0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 0],
 [0, 200, 0, 1, 1, 0],
 [2, 0, 0, 0, 0, 0]]
def Regulator(t):

   return 1