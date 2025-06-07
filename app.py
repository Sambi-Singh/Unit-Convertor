
def inToCm(inputIn):
    toCm = inputIn * 2.54
    print(f"{inputIn} in --> {toCm} cm")
    return
    
def ftToMeter(inputFt):
    toMeter = inputFt/3.281
    print(f"{inputFt} ft --> {toMeter} m")
    return

def lbToKilogram(inputLb):
    toKilogram = inputLb/2.205
    print(f"{inputLb} lb --> {toKilogram} kg")
    return



def startMsg():
    units = {'in': 'cm', 'ft':'m', 'lb':'kg'}
    
    print("**-- Please enter the abbreviation (in, ft, lb, and q to quit) of the unit you wish to convert --**\n")
    for unit in units:
        print(f"{unit} to {units[unit]}")
    print("---------------------")
def main():
    #print("hi")
    while(True):
        startMsg()
        inputVal = input()
        if inputVal.lower() == 'in':
            inches = float(input("Enter value for inches: "))
            inToCm(inches)
        elif inputVal.lower() == 'ft':
            feet = float(input("Enter value for feet: "))
            ftToMeter(feet)
        elif inputVal.lower() == 'lb':
            pounds = float(input("Enter value for pounds: "))
            lbToKilogram(pounds)
        elif inputVal.lower() == 'q':
            print("Qutting now, bye bye :)")
            break
        else:
            print("Error please enter either in, ft, or lb")



if __name__ == '__main__':
    main()

