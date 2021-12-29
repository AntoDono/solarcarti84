def main(voltage):

    if not isinstance(voltage, str):
        Ah = 5000 / voltage
        return Ah
    else:
        print("Please enter a valid voltage (getPAB.py)")
