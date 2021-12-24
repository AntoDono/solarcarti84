import ti_system as ti

def main():
    ti.disp_clr()
    rate = float(input('RATE (MILES PER HOUR): '))
    time = float(input('TIME (HOURS): '))
    print('DIST: '+str(float(rate*time))+' MILES')