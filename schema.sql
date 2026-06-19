CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books(
    BookID INT PRIMARY KEY,
    BookName VARCHAR(100),
    Author VARCHAR(100),
    Quantity INT
);