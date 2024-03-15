num1= int (input("Enter your 1st number: "))
num2= int (input("Enter your 2nd number: "))
op= input("Enter the operation you want to perform: ")

if op =='+':
    print("The sum of your numbers is: ", num1+num2)
elif op =='-':
    print("The difference of your numbers is: ", num1-num2)
elif op =='*':
    print("The product of your numbers is: ", num1*num2)
elif op =='/':
        print("The quotient of your numbers is: ", num1/num2)
else:
    print("The operation is invalid.")