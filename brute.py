from getPAB import getPAB
import getPres
from math import floor

def getPower(batteries, volt_or_ah):
    return batteries * volt_or_ah

def bruteForce(nominal_voltage, battery_type, priority="power", verbose=False):
    battery = getPres.getPres(battery_type)
    if (not battery): return "Invalid Battery Type"

    amp_hours = getPAB(nominal_voltage)  
    parallel = floor(amp_hours/battery["Ah"])
    series = floor(nominal_voltage/battery["nominal-voltage"])
    # parallel = 10
    # series = 10

    # combo = { 'parallel': parallel, 'series': series, 'max: getPower(parallel, battery['Ah']) * getPower(series, battery['nominal-voltage']), 'amp: amp_hours, 'voltage': nominal_voltage }

    combo = [ parallel, series, getPower(parallel, battery['Ah']) * getPower(series, battery['nominal-voltage']),amp_hours, nominal_voltage ]

    maximum_iteration = round(min(parallel, series)/2 + 1)
    # maximum_iteration = 3

    for scenario in range(0, 5):

        if (scenario == 0):
            parallel_change = 1
            series_change = 1
        elif (scenario == 1):
            parallel_change = 1
            series_change = -1
        elif (scenario == 2):
            parallel_change = -1
            series_change = 1
        elif (scenario == 3):
            parallel_change = 0
            series_change = 1
        elif (scenario == 4):
            parallel_change = 1
            series_change = 0


        brute_parallel = parallel
        brute_series = series
        
        if (verbose): print("Current scenario: %f | PC: %f | SC: %f" % (scenario, parallel_change, series_change) )

        for outer in range(0, maximum_iteration ):

            brute_parallel+=parallel_change

            for inner in range(0, maximum_iteration):
                brute_series+=series_change

                brute_nominal = getPower(brute_series, battery['nominal-voltage']) 
                brute_amp = getPower( brute_parallel, battery['Ah'])

                brute_power = brute_nominal * brute_amp

                if (verbose): print("Series: %f | Parallel: %f | Power: %f" % (brute_series, brute_parallel, brute_power))

                if (brute_power <= 5000):
                    applychange = False

                    if (combo[2]<brute_power):
                        if (priority=="amp" and combo[1]<brute_series):
                            applychange = True
                        elif (priority=="voltage" and combo[1]<brute_series):
                            applychange = True
                        else:
                            applychange = True

                    if (applychange):
                        combo[0] = brute_parallel
                        combo[1] = brute_series
                        combo[2] = brute_power
                        combo[3] = brute_amp
                        combo[4] = brute_nominal

                        print("Found new maximum combination: ")
                        print(combo)

            brute_series-= maximum_iteration * series_change
            
        brute_parallel = parallel
        brute_series = series

    return combo

def description():
    return "Brute force best combination for series and parallel"