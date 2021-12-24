import ti_system as ti
from time import *
import Distance
import Velocity
import SCharge


def main():
    ti.disp_clr()
    print('WELCOME TO SUN CALC\n\n')
    MenuItem = input('PLEASE SELECT AN OPTION: \n1 - VEL CALC\n2 - DIST CALC\n3 - SUPERCHARGE CALC\n0 - TO QUIT PROGRAM\n\nCHOICE: ')
    if MenuItem.isdigit():
        MenuItem = int(MenuItem)

        if MenuItem == 1:
            Velocity.main()
            input('\n\n\n\nONCE READY PRESS ANY KEY')
            main()           
        
        elif MenuItem == 2:
            Distance.main()
            input('\n\n\n\nONCE READY PRESS ANY KEY')
            main()
        
        elif MenuItem == 3:
            ti.disp_clr()
            SCharge.main()
            input('\n\n\n\nONCE READY PRESS ANY KEY')
            main()

        elif MenuItem == 0:
            ti.disp_clr()
            print('THANK YOU FOR USING STAR CALC!!\n')
            sleep(2)
            ti.disp_clr()

        else:
            ti.disp_clr()
            print('PLEASE ENTER A VALID OPTION')
            main()
    
    else:
        ti.disp_clr()
        print('PLEASE ENTER A VALID OPTION')
        main()        
        

main()
