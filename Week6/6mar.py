"""
🔹 Array (List) of Objects
In the main program:
• Create at least 3 book objects.
• Store them inside a list of objects called library.
• Perform the following operations:
    • Display all books
    • Issue copies of a book
    • Add copies to a book
    • Calculate total value of all books in the library

Book 1
• Book ID: 101
• Title: Python Programming
• Author: Mark Lutz
• Price: 750
• Copies Available: 5

Book 2
• Book ID: 102
• Title: Data Structures and Algorithms
• Author: Thomas H. Cormen
• Price: 1200
• Copies Available: 3

Book 3
• Book ID: 103
• Title: Machine Learning Basics
• Author: Andrew Ng
• Price: 950
• Copies Available: 4
"""
class Book:
    book_id=0
    title=""
    author=""
    price=0.0
    copies_available=0
    def __init__(self,book_id,title,author,price,copies_available):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.price=price
        self.copies_available=copies_available
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
    def issue_book(self,quantity):
        if quantity>self.copies_available:
            print("Not enough copies available")
        else:
            self.copies_available-=quantity
    def add_copies(self,quantity):
        self.copies_available+=quantity
    def book_value(self):
        return self.price*self.copies_available

def main():
    library=[]
    library.append(Book(101,"Python Programming","Mark Lutz",750,5))
    library.append(Book(102,"Data Structures and Algorithms","Thomas H. Cormen",1200,3))
    library.append(Book(103,"Machine Learning Basics","Andrew Ng",950,4))
    print("All Books in the Library:")
    for book in library:
        book.display_book()
        print()
    print("Issuing 2 copies of 'Python Programming'")
    library[0].issue_book(2)
    
    print("Adding 3 copies to 'Data Structures and Algorithms'")
    library[1].add_copies(3)
    
    print("Total value of all books in the library:")
    total_value=0
    for book in library:
        total_value+=book.book_value()
    print(total_value)

class BookStore:
    def __init__(self,title,author,qty,price):
        self.title=title
        self.author=author
        self.qty=qty
        self.price=price
    def get_data(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Quantity:", self.qty)
        print("Price:", self.price)

def BookStoreMain():
    books=[]
    print("How many books you want to enter?")
    n=int(input())
    for i in range (n):
        print("Enter title,author,quantity and price of book",i+1)
        title=input("Enter title: ")
        author=input("Enter author: ")
        qty=int(input("Enter quantity: "))
        price=float(input("Enter price: "))
        books.append(BookStore(title,author,qty,price))
    for book in books:
        book.get_data()

if __name__=="__main__":
    main()