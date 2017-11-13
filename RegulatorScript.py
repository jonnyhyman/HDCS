def Regulator(t):
    if t>=0 and t <= 0.4:
        return 0.3
    elif t>0.4 and t <= 0.8:
        return 0.6
    elif t>0.8:
        return 1
                        