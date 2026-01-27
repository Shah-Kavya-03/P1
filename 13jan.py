def getnum():
    num = int(input("Enter a number"))
    return num

def pr(num):
    if check(num)%2:
        print(f"{num} is Odd")
    else:
        print("{} is Even".format(num))
    return 

def no(num):
    sum=0
    while num>0:
        sum+=1
        num = num //10
    return sum


def fact(num):
    for i in range(1,num):
        num*=i
    return num

def check(num):
    return bool(num % 2)

def main():
    num = getnum()
    print(no(num))

if __name__=="__main__":
    main()
