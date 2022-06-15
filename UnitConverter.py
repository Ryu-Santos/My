import os
import time

#Unit Converter by yours truly
def Unit1():
    uOne = float(input("Select unit to convert from: \n1.km\n2.m\n3.cm\n4.mm\nEnter the value: "))
    return uOne
def inValue():
    Value = float(input("Enter your value: "))
    return Value
def Unit2():
    uTwo = float(input("Select unit to convert to: \n1.km\n2.m\n3.cm\n4.mm\nEnter the value: "))
    return uTwo

def finalOutput(uOne, Value, uTwo):
    if (uOne == 1):
        if (uTwo == 2):
            print("Kilometer to meter")
            output = Value*1000
            print(f'The final value converted value from {Value:.2f}km is {output}m')
        if (uTwo == 3):
            print("Kilometer to centimeter")
            output = Value*100000
            print(f'The final value converted value from {Value:.2f}km is {output}cm')
        if (uTwo == 4):
            print("Kilometer to millimeter")
            output = Value*1000000
            print(f'The final value converted value from {Value:.2f}km is {output}mm')
    elif (uOne == 2):
        if (uTwo == 1):
            print("Meter to kilometer")
            output = Value/1000
            print(f'The final value converted value from {Value:.2f}m is {output}km')
        if (uTwo == 3):
            print("Meter to centimeter")
            output = Value*100
            print(f'The final value converted value from {Value:.2f}m is {output}cm')
        if (uTwo == 4):
            print("Meter to millimeter")
            output = Value*1000
            print(f'The final value converted value from {Value:.2f}m is {output}mm')
    elif (uOne == 3):
        if (uTwo == 1):
            print("Centimeter to kilometer")
            output = Value/100000
            print(f'The final value converted value from {Value:.2f}cm is {output}km')
        if (uTwo == 2):
            print("Centimeter to meter")
            output = Value/100
            print(f'The final value converted value from {Value:.2f}cm is {output}m')
        if (uTwo == 4):
            print("Centimeter to millimeter")
            output = Value*10
            print(f'The final value converted value from {Value:.2f}cm is {output}mm')
    elif (uOne == 4):
        if (uTwo == 1):
            print("Millimeter to kilometer")
            output = Value/1000000
            print(f'The final value converted value from {Value:.2f}mm is {output}km')
        if (uTwo == 2):
            print("Millimeter to meter")
            output = Value/1000
            print(f'The final value converted value from {Value:.2f}mm is {output}m')
        if (uTwo == 3):
            print("Millimeter to centimeter")
            output = Value/10
            print(f'The final value converted value from {Value:.2f}mm is {output}cm')


def main():
    uOne = Unit1()
    Value = inValue()
    uTwo = Unit2()
    finalOutput(uOne, Value, uTwo)
    restart = input("\n\nDo you want to try again? press G to start again and any characters to exit\nYour selection: ").lower()
    if (restart == 'g' or restart == 'G'):
        os.system('cls')
        main()
    else:
        exit()

main()