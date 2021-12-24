import ti_system as ti

def main():
    ti.disp_clr()
    volt = float(input('VOLT: '))
    print('SUPERCHARGED VOLTS: '+str(volt * 1.16)+' VOLTS')
