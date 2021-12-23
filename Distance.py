import ti_system as ti

def main():
    ti.disp_clr()
    rate = float(input('RATE (MILES PER HOUR): '))
    time = float(input('TIME (HOURS): '))
    distance = float(rate*time)
    print('DIST: '+str(distance)+' MILES')