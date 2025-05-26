import json
import os
from typing import List, Dict, Union


library: List[Dict[str, Union[str, int, bool]]] = []


# File to save/load data
FILE_NAME = "library.txt"

# Load library from file
def load_library():
    global library
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                library = json.load(file)
            except json.JSONDecodeError:
                library = []

# Save library to file
def save_library():
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("❌ Invalid year! Try again.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found!")

# Search for a book
def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the title or author: ").lower()
    found = []

    if choice == "1":
        found = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        found = [book for book in library if keyword in book["author"].lower()]
    else:
        print("❌ Invalid choice.")
        return

    if found:
        print("📚 Matching Books:")
        for i, book in enumerate(found, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found.")

# Display all books
def display_all_books():
    if not library:
        print("📚 Your library is empty.")
        return
    print("📘 Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_statistics():
    total = len(library)
    if total == 0:
        print("📊 No books in the library yet.")
        return
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total) * 100
    print(f"📊 Total books: {total}")
    print(f"📖 Percentage read: {percentage:.1f}%")

# Main Menu
def main():
    load_library()
    while True:
        print("\n📚 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("💾 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
