class Negative(Exception):
    pass
try:
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    if num1<0 or num2<0:
        raise Negative("Negative Number")
    res = num1 / num2 
    print("Result: ",res)
except Exception as e:
    print("Wrong Input:",e)