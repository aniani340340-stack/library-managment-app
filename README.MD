# Library Management System (Python)

## Overview

A Library Management System developed in Python to practice both:

* CRUD Operations (Create, Read, Update, Delete)
* Object-Oriented Programming (OOP)

The project allows users to manage books, issue books, return books, search books, and delete records while maintaining book inventory.

---

## Features

### Add Book

* Add a new book to the library.
* Prevent duplicate Book IDs.

### Search Book

* Search books using Book ID.

### Display Books

* View all books available in the library.

### Issue Book

* Borrow a book from the library.
* Automatically decreases available quantity.
* Prevents issuing books when quantity reaches zero.

### Return Book

* Return a borrowed book.
* Automatically increases available quantity.

### Delete Book

* Remove a book from the library records.

---

## OOP Concepts Used

### Book Class

Stores information related to a single book.

Attributes:

* Book ID
* Book Name
* Author
* Quantity

Methods:

* Constructor (`__init__`)
* String Representation (`__str__`)

### Library Class

Manages all book operations.

Methods:

* add_book()
* borrow_book()
* return_book()
* display_books()

---

## CRUD Operations Implemented

| Operation | Description              |
| --------- | ------------------------ |
| Create    | Add new books            |
| Read      | Search and display books |
| Update    | Issue and return books   |
| Delete    | Remove book records      |

---

## Technologies Used

* Python
* Object-Oriented Programming
* Lists
* Loops
* Conditional Statements
* Functions
* Exception Handling
* CSV/File Handling

---

## Project Structure

```text
Library-Management-System/
│
├── library-management-app.py
├── library-management-app-opp.py
├── booksdata.csv
└── README.md
```

---

## Sample Menu

```text
1. Add Book
2. Search Book
3. Show All Books
4. Issue Book
5. Return Book
6. Delete Book Data
7. Exit
```

---

## Sample Book Object

```text
Book
├── Book ID : 101
├── Name    : Mahabharat
├── Author  : Vyash
└── Quantity: 5
```

---

## Learning Outcomes

Through this project, I learned:

* Object-Oriented Programming
* Classes and Objects
* Constructors (`__init__`)
* Special Methods (`__str__`)
* CRUD Operations
* Inventory Management Logic
* File Handling
* Data Validation
* Search and Update Algorithms

---

## Future Improvements

* Save OOP objects to CSV automatically
* Search by Book Name
* Update Book Details
* Fine Management System
* Student Records
* Issue Date and Return Date
* SQLite Database Integration
* GUI using Tkinter

---

## Author

Anish Agrawal

---

## Project Status

✅ Completed

Part of my Python Development and AI/ML Learning Roadmap.
