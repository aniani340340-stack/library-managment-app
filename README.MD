📚 Library Management System (Python + MySQL)
Overview

A command-line Library Management System built using Python and MySQL. This project allows users to manage library books efficiently using a relational database instead of file storage.

The project demonstrates database connectivity, CRUD operations, SQL queries, input validation, and basic inventory management concepts.

Features

✅ Add New Books

✅ Search Books by Book ID

✅ View All Books

✅ Issue Books

✅ Return Books

✅ Delete Books

✅ Duplicate Book ID Validation

✅ Quantity Availability Check

✅ MySQL Database Integration

✅ Input Validation using Exception Handling

Technologies Used
Python 3
MySQL
MySQL Connector for Python
Project Structure
library-management-app/
│
├── library-management.py
├── schema.sql
├── README.md
├── requirements.txt
Database Schema
Database
CREATE DATABASE library_db;
Table
CREATE TABLE books(
    BookID INT PRIMARY KEY,
    BookName VARCHAR(100),
    Author VARCHAR(100),
    Quantity INT
);
SQL Concepts Used
CREATE DATABASE
CREATE TABLE
INSERT
SELECT
UPDATE
DELETE
WHERE Clause
PRIMARY KEY
Database Constraints
Functionalities
Add Book

Adds a new book to the database while preventing duplicate Book IDs.

Search Book

Searches and displays book details using Book ID.

Show All Books

Displays all books stored in the database.

Issue Book

Reduces available quantity by 1 after validating availability.

Return Book

Increases quantity when a book is returned.

Delete Book

Removes a book record from the database.

Installation
Clone Repository
git clone <repository-url>
Install Dependency
pip install mysql-connector-python

or

pip install -r requirements.txt
Create Database

Run the SQL commands inside schema.sql.

Run Project
python library-management.py
Learning Outcomes

Through this project I learned:

Python Programming
Object-Oriented Thinking
Exception Handling
Database Design
SQL CRUD Operations
Python–MySQL Integration
Working with Relational Databases
Input Validation and Error Handling
Future Enhancements
Student Management Module
Book Issue History
Fine Calculation System
Login Authentication
GUI using Tkinter
Web Version using Flask/Django
Report Generation
Author

Anish Agrawal

B.Tech CSE (Cloud Computing)

SRM Institute of Science and Technology