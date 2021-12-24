import ti_system as ti

def main():
        ti.disp_clr()
        dist = float(input('DIST (MILES): '))
        time = float(input('TIME (HOURS): '))
        print('VEL: '+str(dist/time)+' MPH')