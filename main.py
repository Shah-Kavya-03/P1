from Exception import MyException
import sys
from logger import logging
def main():
    try:
        num1 = int(input("Enter 1st Number: "))
        num2 = int(input("Enter 2nd Number: "))
        res = num1 / num2 
        print("Result: ",res)
    except Exception as e:
        raise MyException(e,sys)
if __name__=="__main__":
    main()