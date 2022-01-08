import ti_system as ti
import getPres as pres
import Main

def main():
    ti.clear()
    voltage = input('BATTERY VOLATGE: ')
    print('WHICH BATTERY?')
    print('[0] - Panasonic NCR18650BD')
    print('[1] - Panasonic-Sayno')
    print('[2] - Sanyo NCR18650GA')
    battery = input('CHOICE: ')

    if type(battery) == 'int':
        print('BATTERIES IN ROW: '+volatge/pres.getPres(battery))
        input('\n\nTYPE ANY KEY TO GO TO MAIN MENU')
        Main.main()
        
    
        
