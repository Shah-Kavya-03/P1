def sort_array():
    num1 = [2,6,8]
    num2 = [1,2,7,8,9]
    num3 = num1 + num2
    for j in range(0,len(num3),1):
        for i in range(0,len(num3)-1,1):
            if num3[i]>num3[i+1]:
                temp = num3[i]
                num3[i]=num3[i+1]
                num3[i+1]=temp
    print(num3)

def search():
    arr = [1,3,5,6,7]
    num = int(input("Enter the number to be searched: "))
    for i in range(0,len(arr),1):
        if arr[i]==num:
            print("Number found at index ",i)
            break

def pair():
    arr = [2,3,3,5,7,8,9]
    num = int(input("Enter the number: "))
    temp=0
    for i in range(0,len(arr),1):
        if temp==1:
            break
        for j in range(i+1,len(arr),1):
            if arr[i]+arr[j]==num:
                temp = 1
                print("Pair found: ",i,",",j)
                break
def max_frequency():
    pre = [2,4,3,2,3,5,6,2]
    count = 0
    max = 0
    for i in range(0,len(pre),1):
        temp = pre[i]
        for j in range(i,len(pre),1):
            if pre[j]==temp:
                count+=1
        if max < count:
            max = count
        count = 0
    print("Maximum frequency is: ",max)

def permut():
    inp1 = int(input("Enter the first number: "))
    inp2 = int(input("Enter the second number: "))
    inp3 = int(input("Enter the third number: "))

    permut=[]
    for i in [inp1, inp2, inp3]:
        for j in [inp1, inp2, inp3]:
            for k in [inp1, inp2, inp3]:
                if i!=j and j!=k and i!=k:
                    permut.append((i, j, k))
    print("All possible permutations are:")
    for p in permut:
        print(p)

def main():
    

if __name__ == "__main__":
    main()