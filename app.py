
def startMsg():
    units = {'in': 'inches', 'ft':'feet', 'lb':'pounds',
             'cm': 'centimeters', 'm': 'meters', 'kg':'kilograms'}
    
    print("**-- Please enter the abbreviation (kg, in, m/s, etc) of the unit you wish to convert --**\n")
    for unit in units:
        print(f"{unit} -- {units[unit]}")
def main():
    #print("hi")
    startMsg()
if __name__ == '__main__':
    main()

