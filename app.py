
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\n✅ Book '{book.title}' added to the library.")

    def show_books(self):
        if not self.books:
            print("\n❌ No books in the library.")
        else:
            print("\n📚 Books in Library:")
            for idx, book in enumerate(self.books):
                print(f"{idx + 1}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"\n✅ You borrowed '{book.title}'.")
                return
        print("\n❌ Book not available or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"\n✅ You returned '{book.title}'.")
                return
        print("\n❌ This book wasn't borrowed or doesn't exist.")

def main():
    library = Library()

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == '2':
            library.show_books()

        elif choice == '3':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
