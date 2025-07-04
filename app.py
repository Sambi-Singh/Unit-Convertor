
#CONVERSION METHODS 
#******************
def inToCm(inputIn):
    toCm = inputIn * 2.54
    print(f"\n{inputIn} in --> {toCm:.2f} cm")
    return
    
def ftToMeter(inputFt):
    toMeter = inputFt/3.281
    print(f"\n{inputFt} ft --> {toMeter:.2f} m\n")
    return

def lbToKilogram(inputLb):
    toKilogram = inputLb/2.205
    print(f"\n{inputLb} lb --> {toKilogram:.2f} kg")
    return



def startMsg():
    units = {'in': 'cm', 'ft':'m', 'lb':'kg'}
    print("---------------------")

    for unit in units:
        print(f"{unit} to {units[unit]}")
    print("---------------------")
def main():
    #print("hi")
    print("\n**-- Please enter the abbreviation (in, ft, lb, and q to quit) of the unit you wish to convert --**\n")

    while(True):
        startMsg()
        inputVal = input()

        #Testing *****
        #inToCm(25.4) #Nothing showing up!
        #*****
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

