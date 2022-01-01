import os
import batttype

try:
    import ti_system as ti
except:
    pass

def clear():
    try:
        ti.disp_clr()
    except:
        os.system('cls')

def printOptions():
    count = 1
    print(str(count) + ". " + "Calculate solar array area")
    count += 1
    print(str(count) + ". " + "Calculate Array Voltage")
    count += 1
    print(str(count) + ". " + "Calculate Amp Hour")
    count += 1
    print(str(count) + ". " + "Calculate Parallel Batteries")
    count += 1
    print(str(count) + ". " + "Calculate Power")
    count += 1
    print(str(count) + ". " + "Calculates Supercharged Voltage")
    count += 1
    print(str(count) + ". " + "Returns velocity")
    count += 1
    print(str(count) + ". " + "Brute force best combination for series and parallel")

def selectBattery():
    clear()
    print("Battery types: ")
    count = 1
    mapBatt = {}
    for batt in batttype.batteries.keys():
        print("%d. %s | V: %s AH: %s" % (count, batt, str(batttype.batteries[batt]['nominal-voltage']), str(batttype.batteries[batt]['Ah'])))
        mapBatt[count] = batt
        count+=1
    choice = isint(input("Select a battery > "))
    return mapBatt[choice]

def isverbose():
    clear()
    print("Verbose on?")
    print("1. Yes")
    print("2. No")
    choice = isint(input("Your response > "))
    if (choice==1): return True
    return False

def choosePriority():
    clear()
    print("Please choose your priority: ")
    print("1. Get Maximum Voltage")
    print("2. Get Maximum Amp Hours")
    print("3. Get Maximum Power")
    choice = isint(input("Select your priority > "))
    if (choice==1): return "voltage"
    elif (choice==2): return "amp"
    elif (choice==3): return "power"

def isint(response):
    try:
        float(response)
        return float(response)
    except:
        clear()
        print("Not an number, press enter to try again.")
        input("Press enter to continue...")
        main()


def main():
    clear()
    print("Staten Island SolarCar\n")
    printOptions()

    choice = isint((input("\nSelect an option > ")))

    if (choice == 1):
        import getArea
        clear()
        cells = isint(input("Please input the number of cells: "))
        area = isint(input("Please input the area of one cell: "))
        result = getArea.getArea(cells, area)
        print("The total area of the solar array is: %f" % (result))
        input("Press enter to continue...")
        clear()
    elif (choice == 2):
        import getArray
        clear()
        cells = isint(input("Please input the number of cells: "))
        volt = isint(input("Please input the voltage of one cell: "))
        result = getArray.getArray(cells, volt)
        print("The total voltage of the solar array is: %f" % (result))
        input("Press enter to continue...")
        clear()
    elif (choice == 3):
        import getPAB
        clear()
        battvolt = isint(input("Please input the battery voltage: "))
        result = getPAB.getPAB(battvolt)
        print("The resulted amp hour is: %f" % (result))
        input("Press enter to continue...")
        clear()
    elif (choice == 4):
        import getPara
        clear()
        battAmp = isint(input("Please input the battery amp hour: "))
        cellAmp = isint(input("Please input the cell amp hour: "))
        result = getPara.getPara(battAmp, cellAmp)
        print("The resulted number of batteries needed are: %f" % (result))
        input("Press enter to continue...")
        clear()
    elif (choice == 5):
        import getPow
        clear()
        arrvolt = isint(input("Voltage of the whole array: "))
        current = isint(input("Please input the current: "))
        result = getPow.getPow(arrvolt, current)
        input("Press enter to continue...")
        print("The power is: {result}")
        clear()
    elif (choice == 6):
        import SCharge

        clear()
        volt = isint(input("Desire voltage: "))
        result = SCharge.getSCharge(volt)
        print("The supercharged voltage is: %f" % (result))
        input("Press enter to continue...")
        clear()
    elif (choice == 7):
        import Velocity

        clear()
        dist = isint(input("Distance traveled (m): "))
        time = isint(input("Elapsed time (s): "))
        result = Velocity.getVelocity(dist, time)
        print("The velocity is: %f m/s" % (result))
        input("Press enter to continue...")
        clear()
    elif (choice==8):
        import brute
        clear()
        nominal_volt = isint(input("Please provide the nominal (desired) voltage: "))
        choice = selectBattery()
        priority = choosePriority()
        verbose = isverbose()
        result = brute.bruteForce(nominal_volt, choice, priority=priority, verbose=verbose)
        print("Best result found:")
        print(result)
        print("===================RESULT=====================")
        print("Batteries in parallel | %f" % (result['parallel']))
        print("Batteries in series | %f" % (result['series']))
        print("Total Voltage | %f" % (result['voltage']))
        print("Batteries in series | %f" % (result['amp']))
        print("Total power | %f" % (result['max']))
        print("==============================================")
        input("Press enter to continue...")

    main()
    
main()