class Book:
    def __init__(self,title, author):
        self.title =title
        self.author = author
        self.is_available = True
        
    def check_out(self):
        if self.is_available:
            self.is_available = False
            print("you borrowed the book:",self.title)
        else:
            print("it's already taken")

    def return_book(self):
        if  not self.is_available:
            self.is_available = True
            print("Book returned :", self.title)
        else:
            print("This book was not borrowed.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self ,book_object):
        self.books.append(book_object)

    def dispaly_books(self):
        for book in self.books:
            print(f"{book.title},{book.author}")
            print(f"{book.is_available}")

    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                print(" Book found:",book.title ,"_",book.author)
                return
            else:
                print("Book not found")


b1 = Book("sathiya","sathiya")
b1.check_out()
#b1.return_book()

lib = Library()
lib.add_book(b1)

lib.find_book("python")

