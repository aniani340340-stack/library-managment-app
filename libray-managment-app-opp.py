class Book:
    def __init__(self,book_id,name,author,quantity):
        self.book_id=book_id
        self.name=name
        self.author=author
        self.quantity=quantity
    def __str__(self):
        return(
            f"book_id:{self.book_id},"
            f"Author:{self.author},"
            f"Name:{self.name},"
            f"quantity:{self.quantity}"
        )    
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"Books {book.book_id} is added to library.")
    def borrow_books(self,id):
        for book in self.books:
            if book.book_id==id:
                if book.quantity>0:
                    book.quantity-=1
                    print(f"You have borrowed {book.name} by {book.author}.")
                else:
                    print(f"Sorry, {book.name} is currently not available for borrowing.")
                return
    def return_book(self,id):
        for book in self.books:
            if book.book_id==id:
                book.quantity+=1
                print(f"You have returned {book.name} by {book.author}.")
                return  
    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)              
            
book1=Book(101,"mahabharat","yashna",5)
book2=Book(102,"ramayan","yashna",3)
print(book1) 
library=Library()
library.add_book(book1) 
library.add_book(book2)

library.borrow_books(101) 
library.return_book(101)
library.display_books()

    
    
       
