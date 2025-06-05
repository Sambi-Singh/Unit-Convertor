
def startMsg():
    units = {'in': 'cm', 'ft':'m', 'lb':'kg'}
    
    print("**-- Please enter the abbreviation (in, ft, lb) of the unit you wish to convert --**\n")
    for unit in units:
        print(f"{unit} to {units[unit]}")
    print("---------------------")
def main():
    #print("hi")
    startMsg()
    inputVal = input()
    if inputVal.lower() == 'in':
        pass
    if inputVal.lower() == 'lb':
        pass

if __name__ == '__main__':
    main()

