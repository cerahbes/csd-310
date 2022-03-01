/*
    Title: whatabook.init.sql
    Author: Roben Johnson
    Date: 3/1/2022
    Description: Initialization script for WhatABook database project
*/

-- create user and set privileges
DROP USER IF EXISTS 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- create tables
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store ( 
    store_id    INT             NOT NULL    AUTO_INCREMENT, 
    locale      VARCHAR(500)    NOT NULL, 
    PRIMARY KEY(store_id));

CREATE TABLE book ( 
    book_id     INT             NOT NULL    AUTO_INCREMENT, 
    book_name   VARCHAR(200)    NOT NULL, 
    author      VARCHAR(200)    NOT NULL, 
    details     VARCHAR(500), 
    PRIMARY KEY(book_id));

CREATE TABLE user ( 
    user_id         INT         NOT NULL    AUTO_INCREMENT, 
    first_name      VARCHAR(75) NOT NULL, 
    last_name       VARCHAR(75) NOT NULL, 
    PRIMARY KEY(user_id));

CREATE TABLE wishlist ( 
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT, 
    user_id         INT         NOT NULL, 
    book_id         INT         NOT NULL, 
    PRIMARY KEY (wishlist_id), 
    CONSTRAINT fk_book 
    FOREIGN KEY (book_id) 
        REFERENCES book(book_id), 
    CONSTRAINT fk_user 
    FOREIGN KEY (user_id) 
        REFERENCES user(user_Id));

-- insert records
INSERT INTO store(locale)
    VALUES('406 S. Main St., Laura, OH 45337');

INSERT INTO book(book_name, author, details)
    VALUES('This is a Book: Volume 1', 'Bob Johnson', 'A brief description about why a good is a book.');
INSERT INTO book(book_name, author, details)
    VALUES('This is a Book: Volume 2', 'Bob Johnson', 'Another stunning depiction of bibliographic works.');
INSERT INTO book(book_name, author, details)
    VALUES('The Search for More', 'Colin Jackson', 'Finding yourself through an examination of history.');
INSERT INTO book(book_name, author, details)
    VALUES('Cooking Shows Make You Eat More!', 'Sally Mae', 'Why do we watch cooking shows if they make us fat?');
INSERT INTO book(book_name, author, details)
     VALUES('This Book is Also Nonsense', 'Robert Fitzguard III', 'Making up fake book records for a database is just the beginning.');
INSERT INTO book(book_name, author, details)
     VALUES('Nine Records: A Lot of Make Believe', 'Will E Sanders', 'The art of crafting words into sentences that might also mean nothing.');
INSERT INTO book(book_name, author, details)
     VALUES('500 Characters Is Not Enough', 'Eddy Extreme', 'Limits are made to be broken and Eddy Extreme says so.');
INSERT INTO book(book_name, author, details)
    VALUES('What Should Your 8th Record Be?', 'Lammy Unger', 'A far reaching dramatization of the struggles of modern programming.');
INSERT INTO book(book_name, author, details)
     VALUES('The Final Entry', 'Annie Moss', 'There are lots of books in the world, but this is the last one.');

INSERT INTO user(first_name, last_name)
    VALUES('Mike', 'Beck');
INSERT INTO user(first_name, last_name)
    VALUES('Jeff', 'Wolfe');
INSERT INTO user(first_name, last_name)
    VALUES('Nathaniel', 'Weiser');

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Mike'),
        (SELECT book_id FROM book WHERE book_name = 'Nine Records: A Lot of Make Believe'));
INSERT INTO wishlist(user_id, book_id)
     VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jeff'),
        (SELECT book_id FROM book WHERE book_name = 'This is a Book: Volume 1'));
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Nathaniel'),
        (SELECT book_id FROM book WHERE book_name = 'The Final Entry'));

