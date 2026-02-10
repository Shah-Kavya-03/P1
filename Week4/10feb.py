#Average Salary Excluding Min and Max
def average_salary():
    employees = [
        {"name": "A", "salary": 30000},
        {"name": "B", "salary": 50000},
        {"name": "C", "salary": 40000},
        {"name": "D", "salary": 60000}
    ]
    salaries = list(map(lambda x: x['salary'], employees))
    min_salary = min(salaries)
    max_salary = max(salaries)
    filtered_salaries = list(filter(lambda x: x != min_salary and x != max_salary, salaries))
    average_salary = sum(filtered_salaries) / len(filtered_salaries)
    print(average_salary)

#Filter Valid Email Domains
def valid_email():
    emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
    allowed_domains = {"gmail.com"}
    valid_emails = list(filter(lambda email: email.split('@')[1] in allowed_domains, emails))
    valid_emails = list(map(lambda email: email.split('@')[0], valid_emails))
    print(valid_emails)

#Students Passed All Subjects
def students_passed():
    students = {"Alice": [45, 50, 60],"Bob": [35, 55, 65],"Charlie": [40, 40, 40]}
    passed_students = list(filter(lambda item: all(mark >= 40 for mark in item[1]), students.items()))
    passed_students = list(map(lambda item: item[0], passed_students))
    print(passed_students)

#Convert & Filter Product Prices
def products():
    products = [("Pen", 10),("Bag", 50),("Shoes", 60)]
    converted_products = list(map(lambda x: (x[0], x[1] * 83), products))
    filtered_products = list(filter(lambda x: x[1] > 3000, converted_products))
    print(converted_products)
    print(filtered_products)

#Active Users with Prime IDs
def prime_users():
    users = [
        {"name": "A", "user_id": 2, "active": True},
        {"name": "B", "user_id": 4, "active": True},
        {"name": "C", "user_id": 5, "active": False},
        {"name": "D", "user_id": 7, "active": True}
    ]
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    active_users = list(filter(lambda user: user['active'] and is_prime(user['user_id']), users))
    active_user_names = list(map(lambda user: user['name'], active_users))
    print(active_user_names)

#Normalize and Filter Strings
def normalize():
    words = ["  Python ", " AI ", "Machine ", " Data "]
    normalize = list(map(lambda x: x.strip().lower(), words))
    filtered = list(filter(lambda x: len(x) >= 5, normalize))
    print(normalize)
    print(filtered)

#1
def num_char():
    def num_char(num):
        return chr(num)
    numbers=[72,69,76,76,79]
    characters=map(num_char, numbers)
    print(list(characters))

#2
def char_num():
    def ascii(char):
        return ord(char)
    characters = ['A','B','C','D']
    ascii_val = map(ascii, characters)
    print(list(ascii_val))

#3
def square():
    def sq(num):
        return num**2
    nums=[2,4,6,8]
    square=map(sq,nums)
    print(list(square))

#4
def vowels():
    def vowel(n):
        v=['a','e','i','o','u']
        if n in v:
            return True
        else:
            return False
    lis=['a','b','c','d','e',]
    vowels=filter(vowel,lis)
    for i in vowels:
        print(i)

#5
def even_odd():
    mylist=[1,2,3,4,5,6,7,8,9]
    even = list(filter(lambda n:n%2==0,mylist))
    print(even)
    odd = list(filter(lambda n:n%2!=0,mylist))
    print(odd)

#6
import functools
def fact():
    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return functools.reduce(lambda x,y:x*y, range (1,n+1))
    print(factorial(3))

#7
def upper_name():
    city=['mumbai','delhi','kolkata']
    low=list(map(lambda x:x.upper(),city))
    print(low)

#8
def sum_list():
    list=[1,3,7,8,10]
    m=functools.reduce(lambda a,b:a+b,list)
    print("sum:",m)

#9
def max_list():
    list=[1,3,7,8,10]
    m=functools.reduce (lambda a,b:a if a>b else b,list)
    print("The maximum is :",m)

def main():
    fact()

if __name__ == "__main__":    
    main()