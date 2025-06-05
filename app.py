
def inToCm(input):
    pass
def ftToMeter(input):
    pass
def lbToKilogram(input):
    pass

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
            pass
        elif inputVal.lower() == 'ft':
            pass
        elif inputVal.lower() == 'lb':
            pass
        elif inputVal.lower() == 'q':
            print("Qutting now, bye bye :)")
            break
        else:
            print("Error please enter either in, ft, or lb")



if __name__ == '__main__':
    main()

