def ty():
    a=2
    b=3.4
    c=True
    d="Apple"
    e=[2,'app',False]
    f={1:"Sunday",2:"Monday"}
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))

def conv():
    num_int=123
    num_flo=1.23
    num_new=num_int+num_flo
    print("Value of num_new",num_new)
    print("Type of num_new",type(num_new))

def seggr():
    marks = [23,65,85,29,78,93,46,62,39]
    A_grade=[]
    B_grade=[]
    C_grade=[]
    for i in marks:
        if i > 80:
            A_grade.append(i)
        elif i>=50 and i<=80:
            B_grade.append(i)
        else:
            C_grade.append(i)
    for i in A_grade:
        print("A Grade marks = ",i)
    for i in B_grade:
        print("B Grade marks = ",i)
    for i in C_grade:
        print("C Grade marks = ",i)

def bill():
    units = int(input("Enter the units used: "))
    if units <= 100:
        print("Your bill is Rs. ",units)
    elif units>100 and units<=200:
        bill=100+(2*(units-100))
        print("Your Bill is Rs. ",bill)
    else:
        bill=300+(3*(units-200))
        print("Your Bill is Rs. ",bill)

def cumulative():
    num=[3,5,2,4,1]
    res=[]
    sum=0
    for i in num:
        sum+=i
        res.append(sum)
    print(res)

def unique():
    input = [2,5,4,2,8,9,5,6,3,2,4]
    res=[]
    for i in input:
        if input.count(i)>=1 and i not in res:
            res.append(i)
    print(res)

def dup():
    input = [2,5,4,2,8,9,5,6,3,2,4]
    res=[]
    for i in input:
        if input.count(i)>1:
            input.pop(i)
    print(input)

def main():
    dup()
if __name__=="__main__":
    main()