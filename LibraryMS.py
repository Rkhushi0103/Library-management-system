class BookNode:
    def __init__(self, book_id, title, author):  
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        self.next = None

class Library:
    def __init__(self):   
        self.head = None

    # Add a new book
    def addBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"Book '{title}' added successfully.")

    # Delete a book by ID
    def deleteBook(self, book_id):
        temp = self.head
        prev = None
        while temp:
            if temp.book_id == book_id:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Book ID {book_id} deleted successfully.")
                return
            prev = temp
            temp = temp.next
        print("Book not found.")

    # Search a book by ID
    def searchBook(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                status = "Available" if temp.available else "Issued"
                print(f"Book found → {temp.book_id}: {temp.title} by {temp.author} [{status}]")
                return temp
            temp = temp.next
        print("Book not found.")
        return None

    # Display all books
    def displayBooks(self):
        if self.head is None:
            print("Library is empty.")
            return
        temp = self.head
        print("\nLibrary Books:")
        while temp:
            status = "Available" if temp.available else "Issued"
            print(f"{temp.book_id}: {temp.title} by {temp.author} [{status}]")
            temp = temp.next

# Stack implementation 
class IssuedStack:
    def __init__(self):   
        self.stack = []

    def push(self, book):
        self.stack.append(book)
        print(f"Book '{book.title}' issued and added to history.")

    def pop(self):
        if not self.stack:
            print("No issued books in history.")
        else:
            book = self.stack.pop()
            print(f"Removed from history: {book.title}")
            return book

    def peek(self):
        if not self.stack:
            print("No issued books.")
        else:
            book = self.stack[-1]
            print(f"Last issued book: {book.title}")

    def display(self):
        if not self.stack:
            print("No issued books history.")
        else:
            print("\nRecently Issued Books:")
            for book in reversed(self.stack):
                print(f"{book.book_id}: {book.title} by {book.author}")

# Menu System
library = Library()
issued_stack = IssuedStack()

while True:
    print("\n===== Library Management Menu =====")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Issue Book")
    print("6. Show Recently Issued Books")
    print("7. Return Book")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice (1-8): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 8.")
        continue

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        library.addBook(book_id, title, author)

    elif choice == 2:
        book_id = int(input("Enter Book ID to delete: "))
        library.deleteBook(book_id)

    elif choice == 3:
        book_id = int(input("Enter Book ID to search: "))
        library.searchBook(book_id)

    elif choice == 4:
        library.displayBooks()

    elif choice == 5:
        book_id = int(input("Enter Book ID to issue: "))
        book = library.searchBook(book_id)
        if book and book.available:
            book.available = False
            issued_stack.push(book)
        else:
            print("Book not available for issue.")

    elif choice == 6:
        issued_stack.display()

    elif choice == 7:
        book_id = int(input("Enter Book ID to return: "))
        book = library.searchBook(book_id)
        if book and not book.available:
            book.available = True
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("This book was not issued or does not exist.")

    elif choice == 8:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1-8.")
