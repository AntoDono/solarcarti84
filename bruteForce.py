import getPAB
from getPara import getPara
import getPres
import math

def getPower(batteries, volt_or_ah):
    return batteries * volt_or_ah

def bruteForce(nominal_voltage, battery_type, priority="power", verbose=False):
    battery = getPres.getPres(battery_type)
    if (not battery): return "Invalid Battery Type"

    amp_hours = getPAB.getPAB(nominal_voltage)
    parallel = math.floor(amp_hours/battery["Ah"])
    series = math.floor(nominal_voltage/battery["nominal-voltage"])

    combo = { 'parallel': parallel, 'series': series, 'max': getPower(parallel, battery['Ah']) * getPower(series, battery['nominal-voltage']), 'amp': amp_hours, 'voltage': nominal_voltage }

    maximum_iteration = round(min(parallel, series)/2 + 1)

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
        
        if (verbose): print(f"Current scenario: {scenario} | PC: {parallel_change} SC: {series_change}")

        for outer in range(0, maximum_iteration ):

            brute_parallel+=parallel_change

            for inner in range(0, maximum_iteration):
                brute_series+=series_change

                brute_nominal = getPower(brute_series, battery['nominal-voltage']) 
                brute_amp = getPower( brute_parallel, battery['Ah'])

                brute_power = brute_nominal * brute_amp

                if (verbose): print(f"Series: {brute_series} | Parallel: {brute_parallel} | Power: {brute_power}")

                if (brute_power <= 5000):
                    applychange = False

                    if (combo['max']<brute_power):
                        if (priority=="amp" and combo['series']<brute_series):
                            applychange = True
                        elif (priority=="voltage" and combo['series']<brute_series):
                            applychange = True
                        else:
                            applychange = True

                    if (applychange):
                        combo['parallel'] = brute_parallel
                        combo['series'] = brute_series
                        combo['max'] = brute_power
                        combo['amp'] = brute_amp
                        combo['voltage'] = brute_nominal

                        print("Found new maximum combination: ")
                        print(combo)

            brute_series-= maximum_iteration * series_change
            
        brute_parallel = parallel
        brute_series = series

    return combo

def description():
    return "Brute force best combination for series and parallel"