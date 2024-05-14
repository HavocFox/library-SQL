CREATE DATABASE library_db;
USE library_db;

CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    publication_date DATE NOT NULL,
    availability BOOLEAN DEFAULT 1,
    returndate DATE NOT NULL
);

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    libid VARCHAR(13) NOT NULL
);

CREATE TABLE Authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    bio TEXT NOT NULL
);

# BASE AUTHORS LIBRARY (Edit as desired) - Don't forget to re-run after using the debug deletions
INSERT INTO Authors (name, bio) VALUES
('Jane Austen', 'Jane Austen was an English novelist known primarily for her six major novels, which interpret, critique and comment upon the British landed gentry at the end of the 18th century.'),
('Charles Dickens', 'Charles Dickens was an English writer and social critic. He created some of the world\'s best-known fictional characters and is regarded by many as the greatest novelist of the Victorian era.'),
('Harper Lee', 'Harper Lee was an American novelist best known for her novel "To Kill a Mockingbird", which deals with the issues of racism that she observed as a child in her hometown of Monroeville, Alabama.'),
('J.K. Rowling', 'J.K. Rowling is a British author, philanthropist, film producer, television producer, and screenwriter. She is best known for writing the Harry Potter fantasy series.'),
('George Orwell', 'George Orwell was an English novelist, essayist, journalist and critic, whose work is marked by lucid prose, awareness of social injustice, opposition to totalitarianism, and outspoken support of democratic socialism.');

# BASE BOOKS LIBRARY (Edit as desired) - Don't forget to re-run after using the debug deletions
INSERT INTO Books (title, author, isbn, genre, publication_date, returndate) VALUES
('Pride and Prejudice', 'Jane Austen', '9780141439518', 'Romance', '1813-01-28', CURDATE()),
('Great Expectations', 'Charles Dickens', '9780141439563', 'Fiction', '1861-11-26', CURDATE()),
('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 'Classic', '1960-07-11', CURDATE()),
('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', '9780590353427', 'Fantasy', '1997-06-26', CURDATE()),
('1984', 'George Orwell', '9780451524935', 'Science Fiction', '1949-06-08', CURDATE());


# Don't use this, it is DEBUG ONLY to reset the program's data testing
DROP TABLE IF EXISTS testing_borrowedbooks;


DELETE FROM Books WHERE 1;
DELETE FROM Users WHERE 1;
DELETE FROM Authors WHERE 1;

