
# which state variables are not instrumentation
Control_Keys = ['A','B','F1','I','R',
                'u1','u2','adcs','hdcs',
                'E','a','F1','F2','B1','B2',
                'Cm']

 # which control variables are actionable via adcs
Command_Keys = ['E','a','F1','F2','B1','B2','c1','c1_','c2','c2_','Cm',
                'TM','UC','RS']

State = {
    'E'   :  0, # Emergency STOP
    'a'   :  0, # Arm Mode
    'F1'  :  0, # Fire Suppression 1
    'F2'  :  0, # Fire Suppression 2
    'c1'   :  0, # Count Timer 1
    'c1_'  :  0, # Count microseconds
    'c2'   :  0, # Count Timer 2
    'c2_'  :  0, # Count microseconds
    'Cm'  :  0, # Count Mode (Halt,Count,Set)
    'TM'  :  0, # Test matrix upload trigger
    'ER'  :  0, # Exceeded range trigger
    'UC'  :  0, # Microcontroller upload trigger
    'RS'  :  0, # ADCS / Microcontroller resetting trigger
    'B1'  :  0, # Bus 1 (Control to v1)
    'B2'  :  0, # Bus 2 (Control to v2)
    'g'   : -1,
    'z0'  : -1,
    'z1'  : -1,
    'z2'  : -1,
    'z3'  : -1,
    'v0'  : -1,
    'v1'  : -1,
    'v2'  : -1,
    'i1'  : -1,
    'i2'  : -1,
    'm0'  : -1,
    'p0'  : -1,
    'p1'  : -1,
    't0'  : -1,
    't1'  : -1,
    't2'  : -1,
    'dt'  : -1,
    'it'  : -1,
    'Fa1' :  0,
    'Fa2' :  0,
    'A'   :  0,
    'B'   :  0,
    'I'   :  0,
    'R'   :  0,
    'u1'  :  0,
    'u2'  :  0,
    'u3'  :  0,
    'u4'  :  0,
    'adcs':  0,
    'hdcs':  0,
    # Below here are ADCS "GENERATED"/calculated variables
    'H'   :  0, # constantly overriden per check
    'C1'  :  0, # u1 count
    'C2'  :  0, # u2 count
    'C1-2':  0, # c1-c2
    # Below here are HDCS "GENERATED"/calculated variables
    'count': -30,
    'zf'  : -1,
    'xf0' : -1,
    'xf1' : -1,
    'yf0' : -1,
    'yf1' : -1,

    'dm0' : -1,
    'l_m0': -1,

    'Rn'  :  0,
    'Rbool': 0,
}

Command={}
for key in State.keys():
    if key in Command_Keys:
        Command[key] = 0

State_Limits = {
    'g'   : [-5,5],
    'z0'  : [-500,500],
    'z1'  : [-500,500],
    'z2'  : [-500,500],
    'z3'  : [-500,500],
    'v0'  : [3.4,5.1],
    'v1'  : [11,13],
    'v2'  : [11,13],
    'i1'  : [-30, 30],
    'i2'  : [-15, 15],
    'm0'  : [-500,500],
    'p0'  : [-10, 17.3],
    'p1'  : [-344.7,344.7],
    't0'  : [-20,50],
    't1'  : [-300,300],
    't2'  : [-300,300],
    'dt'  : [-1, 1],
    'it'  : [0,50],
    'C1-2': [-1,0.035],
    # HDCS Generated State Variable Limits
    'zf'  : [-50,50],
    'xf0' : [-10,10],
    'xf1' : [-10,10],
    'yf0' : [-10,10],
    'yf1' : [-10,10],
    'dm0' : [-1000,1000],
}

State_Limits_keys = State_Limits.keys()

#----------------------------------------------------- HDCS ONLY

Alarms = {  'warning':[],
            'caution':[],
         }

Alarms_Disable = {  'warning':[],
                    'caution':[],
                 }

# The eval string context here has "cmd" and "state" as local variables!
Persist_Criteria = {

    'E' :["state['E']==cmd['E']"],
    'a' :["state['a']==cmd['a']"],
    'Cm':["state['Cm']==cmd['Cm']"],
    'F1':["state['F1']==cmd['F1']"],

}
