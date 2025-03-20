import os

# File to store book data
LIBRARY_FILE = "library.txt"

# Function to load books from the file
def load_books():
    books = []
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    title = parts[0].split(": ")[1]
                    author = parts[1].split(": ")[1]
                    year = int(parts[2].split(": ")[1])
                    genre = parts[3].split(": ")[1]
                    read_status = parts[4].split(": ")[1] == "True"
                    books.append({
                        "title": title,
                        "author": author,
                        "year": year,
                        "genre": genre,
                        "read": read_status
                    })
    return books

# Function to save books to the file
def save_books(books):
    with open(LIBRARY_FILE, "w") as file:
        for book in books:
            file.write(f"Title: {book['title']} | Author: {book['author']} | "
                       f"Year: {book['year']} | Genre: {book['genre']} | Read: {book['read']}\n")

# Function to add a book
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    if not title or not author or not year.isdigit():
        print("Invalid input. Please try again.")
        return
    
    books.append({
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read
    })
    save_books(books)
    print(f"Book '{title}' added successfully!")

# Function to remove a book
def remove_book(books):
    title = input("Enter the title of the book to remove: ").strip()
    filtered_books = [book for book in books if book["title"].lower() != title.lower()]
    
    if len(filtered_books) == len(books):
        print("Book not found.")
    else:
        save_books(filtered_books)
        print(f"Book '{title}' removed successfully!")

# Function to search for a book
def search_book(books):
    search_term = input("Enter book title or author to search: ").strip().lower()
    results = [book for book in books if search_term in book["title"].lower() or search_term in book["author"].lower()]
    
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} | Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No matching books found.")

# Function to display all books
def display_books(books):
    if not books:
        print("Your library is empty.")
        return
    
    print("\nYour Library:")
    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} | Read: {'Yes' if book['read'] else 'No'}")

# Function to display statistics
def display_statistics(books):
    if not books:
        print("No books in the library.")
        return
    
    total_books = len(books)
    read_books = sum(1 for book in books if book["read"])
    read_percentage = (read_books / total_books) * 100
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({read_percentage:.2f}%)")

# Main menu function
def main():
    books = load_books()
    
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            display_statistics(books)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
