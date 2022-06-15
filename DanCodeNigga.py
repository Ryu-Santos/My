# Ortega, Dan Joseph, A / 202102072 / BSCS 1-3 / November 3, 2021 / DCIT22 MIDTERM EXAM
import os
import time
def entName():
    name = input("\033[1;37;40mEnter your full name: ")
    return name
def entRate():
    rate = float(input("\033[1;37;40mEnter your rate: "))
    return rate
def enthrs():
    hours = float(input("\033[1;37;40mHow Many Hours did you work for: "))
    return hours
def entEmpCode():
    empCode = input("\033[1;37;40mEmployee code? (Type A for full time or B for part-time): ").lower()
    return empCode
def entSttCode():
    sttCode = input("\033[1;37;40mState code? (Type Y for New York or J for New Jersey): ").lower()
    return sttCode

def finalOutput(name, rate, hours, empCode, sttCode):
    if (hours<=40):
        rPay=rate*hours
        overTime=0
        gPay=rPay+overTime
        print(f'Hi {name}')
        print(f'Your Regular Pay: {rPay:.2f}')
        print(f'Your Overtime Pay: {overTime:.2f}')
        print(f'Your Gross Pay: {gPay:.2f}')
        if (empCode == 'A' or empCode == 'a'):
            if (sttCode == 'y'):
                tax = 0.07
                updTax=(gPay*tax)
                eNetSalary=gPay-updTax
                print(f'Your Tax: {updTax:.2f}')
                print(f'Your Net Pay: {eNetSalary:.2f}')
            if (sttCode == 'j'):
                tax = 0.045
                updTax=(gPay*tax)
                eNetSalary=gPay-updTax
                print(f'Your Tax: {updTax:.2f}')
                print(f'Your Net Pay: {eNetSalary:.2f}')
        elif (empCode == 'B' or empCode == 'b'):
            tax = 0
            updTax = (gPay * tax)
            eNetSalary = gPay - updTax
            print(f'Your Tax: {updTax:.2f}')
            print(f'Your Net Pay: {eNetSalary:.2f}')
    elif (hours > 40):
        overTime = (1.5 * rate * hours) / 40
        rPay = rate * 40
        gPay = rPay + overTime
        print(f'Hi {name}')
        print(f'Your Regular Pay: {rPay:.2f}')
        print(f'Your Overtime Pay: {overTime:.2f}')
        print(f'Your Gross Pay: {gPay:.2f}')
        if (empCode == 'A' or empCode == 'a'):
            if (sttCode == 'y'):
                tax = 0.07
                updTax=(gPay*tax)
                eNetSalary=gPay-updTax
                print(f'Your Tax: {updTax:.2f}')
                print(f'Your Net Pay: {eNetSalary:.2f}')
            if (sttCode == 'j'):
                tax = 0.045
                updTax=(gPay*tax)
                eNetSalary=gPay-updTax
                print(f'Your Tax: {updTax:.2f}')
                print(f'Your Net Pay: {eNetSalary:.2f}')
        elif (empCode == 'B' or empCode == 'b'):
            tax = 0
            updTax = (gPay * tax)
            eNetSalary = gPay - updTax
            print(f'Your Tax: {updTax:.2f}')
            print(f'Your Net Pay: {eNetSalary:.2f}')

def main():
    name = entName()
    time.sleep(1)
    os.system('cls')
    rate = entRate()
    time.sleep(1)
    os.system('cls')
    hours = enthrs()
    time.sleep(1)
    os.system('cls')
    empCode = entEmpCode()
    time.sleep(1)
    os.system('cls')
    sttCode = entSttCode()
    time.sleep(1)
    os.system('cls')
    choice = input('Do you want to see the summary? Y/N ').lower()
    time.sleep(1)
    os.system('cls')
    if (choice == 'Y' or choice == 'y'):
        finalOutput(name, rate, hours, empCode, sttCode)
        restart = input("\n\n\033[1;37;40mDo you want to try again? press G to start again and any characters to exit\nYour selection: ").lower()
        if (restart == 'g' or restart == 'G'):
            os.system('cls')
            main()
        else:
            exit()
    elif (choice == 'N' or choice == 'n'):
        time.sleep(1)
        restart = input("\n\n\033[1;37;40mDo you want to try again? press G to start again and any characters to exit\nYour selection: ").lower()
        if (restart == 'g' or restart == 'G'):
            os.system('cls')
            main()
        else:
            exit()
    else:
        print('Invalid Selection')
        time.sleep(1)
        restart = input("\n\n\033[1;37;40mDo you want to try again? press G to start again and any characters to exit\nYour selection: ").lower()
        if (restart == 'g' or restart == 'G'):
            os.system('cls')
            main()
        else:
            exit()
main()
