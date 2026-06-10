# Library Management System

## Overview

A command-line Library Management System built using Python and CSV file handling. This project allows users to manage books in a library, including adding books, searching books, issuing books, returning books, and deleting book records.

---

## Features

### Add Book

* Add a new book to the library.
* Prevents duplicate Book IDs.

### Search Book

* Search for a book using its Book ID.

### Show All Books

* Display all books available in the library.

### Issue Book

* Issue a book to a user.
* Reduces the available quantity by 1.
* Prevents issuing when quantity is 0.

### Return Book

* Return a previously issued book.
* Increases the available quantity by 1.

### Delete Book

* Remove a book record from the library.

### Exit

* Safely exit the application.

---

## Technologies Used

* Python
* CSV File Handling
* Loops
* Conditional Statements
* Exception Handling
* CRUD Operations

---

## File Structure

```text
Library-Management-System/
│
├── library_management.py
├── booksdata.csv
├── temparorydata.csv
└── README.md
```

---

## CSV Format

### booksdata.csv

```text
BookID,BookName,Author,Quantity
```

Example:

```text
101,Python Basics,Guido van Rossum,5
102,C++ Programming,Bjarne Stroustrup,3
103,Data Science,Andrew Ng,2
```

---

## Menu

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

## Concepts Learned

* CRUD Operations
* File Handling
* CSV Processing
* Search Algorithms
* Inventory Management
* Business Logic
* Data Validation
* Exception Handling

---

## Future Improvements

* Update Book Details
* Search by Book Name
* Date of Issue and Return
* Student Records
* Fine Calculation System
* Object-Oriented Programming (Classes & Objects)
* Database Integration (SQLite/MySQL)

---

## Author

Anish Agrawal

---

## Project Status

Completed as part of a Python Programming Learning Roadmap.
