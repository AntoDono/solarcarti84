import ti_system as ti

def main():
    ti.disp_clr()
    volt = float(input('VOLT: '))
    supercharge = volt * 1.16
    print('SUPERCHARGED VOLTS: '+str(supercharge)+' VOLTS')
