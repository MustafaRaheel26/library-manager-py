import json
import os

LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {"title": title, "author": author, "year": int(year), "genre": genre, "read": read_status}
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def update_book(library):
    title = input("Enter the title of the book to update: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print(f"Updating {book['title']} by {book['author']}")
            book["title"] = input("New title (leave blank to keep current): ").strip() or book["title"]
            book["author"] = input("New author (leave blank to keep current): ").strip() or book["author"]
            book["year"] = int(input("New publication year (leave blank to keep current): ").strip() or book["year"])
            book["genre"] = input("New genre (leave blank to keep current): ").strip() or book["genre"]
            print("Book updated successfully!")
            return
    print("Book not found.")

def mark_book_status(library):
    title = input("Enter the title of the book to mark as read/unread: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            book["read"] = not book["read"]
            print(f"Book marked as {'Read' if book['read'] else 'Unread'}.")
            return
    print("Book not found.")

def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        keyword = input("Enter the title: ").strip().lower()
        results = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        keyword = input("Enter the author: ").strip().lower()
        results = [book for book in library if keyword in book["author"].lower()]
    else:
        print("Invalid choice!")
        return

    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def sort_books(library):
    print("Sort by:\n1. Title\n2. Author\n3. Year")
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        library.sort(key=lambda book: book["title"].lower())
    elif choice == "2":
        library.sort(key=lambda book: book["author"].lower())
    elif choice == "3":
        library.sort(key=lambda book: book["year"])
    else:
        print("Invalid choice!")
        return
    
    print("Books sorted successfully!")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    print(f"Total books: {total_books}\nPercentage read: {read_percentage:.2f}%")

def export_books(library):
    with open("library_export.txt", "w") as file:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            file.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}\n")
    print("Library exported successfully!")

def main():
    library = load_library()

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Update book details")
        print("4. Mark book as read/unread")
        print("5. Search for a book")
        print("6. Display all books")
        print("7. Sort books")
        print("8. Display statistics")
        print("9. Export books")
        print("10. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            update_book(library)
        elif choice == "4":
            mark_book_status(library)
        elif choice == "5":
            search_books(library)
        elif choice == "6":
            display_books(library)
        elif choice == "7":
            sort_books(library)
        elif choice == "8":
            display_statistics(library)
        elif choice == "9":
            export_books(library)
        elif choice == "10":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
