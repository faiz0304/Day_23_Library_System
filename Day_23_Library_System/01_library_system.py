# Project: Library System (Book Issue/Return using OOP)
# Day: 23 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi
# Goal:
#   - Create a Library class with book issue and return functionality
#   - Use OOP concepts like classes, objects, methods
#   - Practice dictionary data handling

from typing import List, Dict


class Library:
    def __init__(self, books_list: List[str]):
        """Initialize library with a list of books and empty lending record."""
        self.books_list: List[str] = books_list
        self.lend_data: Dict[str, str] = {}  # book_name: user_name

    def display_books(self) -> None:
        """Display all available books."""
        print("\nAvailable Books:")
        for book in self.books_list:
            print(f" - {book}")

    def add_book(self, book: str) -> None:
        """Add a new book to the library."""
        if book not in self.books_list:
            self.books_list.append(book)
            print(f"'{book}' added successfully.")
        else:
            print(f"'{book}' is already in the library.")

    def lend_book(self, book: str, user: str) -> None:
        """Issue a book to a user if available."""
        if book not in self.books_list:
            print(f"'{book}' is not available in the library.")
        elif book not in self.lend_data:
            self.lend_data[book] = user
            print(f"'{book}' has been issued to {user}.")
        else:
            print(f"Sorry, '{book}' is already issued to {self.lend_data[book]}.")

    def return_book(self, book: str) -> None:
        """Return a previously issued book."""
        if book in self.lend_data:
            self.lend_data.pop(book)
            print(f"'{book}' has been returned successfully.")
        else:
            print(f"'{book}' was not issued from this library.")


def main(library: Library) -> None:
    """Main user menu loop."""
    while True:
        print("\n====== Library Menu ======")
        print("1. Show Books of Library")
        print("2. Add Book to Library")
        print("3. Lend Book from Library")
        print("4. Return Book to Library")
        print("5. Exit from Library")

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            library.display_books()

        elif choice == "2":
            book = input("Enter Book Name to Add: ").strip()
            library.add_book(book)

        elif choice == "3":
            book = input("Enter Book Name to Lend: ").strip()
            user = input("Enter Your Name: ").strip()
            library.lend_book(book, user)

        elif choice == "4":
            book = input("Enter Book Name to Return: ").strip()
            library.return_book(book)

        elif choice == "5":
            print("Thanks for visiting our library!")
            break

        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    books: List[str] = ["Python Basics", "C++ OOP", "Data Science", "AI Fundamentals"]
    library = Library(books)
    main(library)
