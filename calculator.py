num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

def calculator(num1, num2):
    
    print("\n\tPress 1 for addition")
    print("\tPress 2 for substraction")
    print("\tPress 3 for multiplication")
    print("\tPress 4 for division ")
    print("\tPress 5 for floor division ")
    print("\tPress 6 for remainders")
    print("\tPress 7 for exponent\n")
    ch = int(input("Enter your choice: "))
    
    if ch==1:
        print(f"\nThe sum of {num1} and {num2} is {num1+num2}")
    elif ch==2:
        print(f"\nThe difference of {num1} and {num2} is {num1-num2}")
    elif ch==3:
        print(f"\nThe product of {num1} and {num2} is {num1*num2}")
    elif ch==4:
        print(f"\nThe quotient of {num1} to the {num2} is {num1/num2}")
    elif ch==5:
        print(f"\nThe floor division  of {num1} to the {num2} is {num1//num2}")
    elif ch==6:
        print(f"\nThe remainder of {num1} and {num2} is {num1%num2}")
    elif ch==7:
        print(f"\nThe exponent of {num1} to the {num2} is {num1**num2}")
    else:
        raise ValueError("Please Enter valid choice number!!!")
        
calculator(num1, num2)

while(True):
    print("\n\tPress 1* for further calculation")
    print("\tPress 2* for further calculation on new number")
    print("\tPress 12* for quit this program\n")
    cho = input("Enter your new choice: ")
    print("\n")
    
    if cho=="1*":
        calculator(num1, num2)
    elif cho=="2*":
        numb1 = int(input("Enter your 1st new number: "))
        numb2 = int(input("Enter your 2nd new number: "))
        calculator(numb1, numb2)
    elif cho=="12*":
        print("Thanks for using calculator !!!")
        break
    else:
         raise VlaueError("Please Enter valid choice numbe!!!")
    