import mysql.connector
from mysql.connector import errorcode

config = {
        "user": "root",
        "password": "sailorV1!isgreat",
        "host": "127.0.0.1",
        "database": "whatabook",
        "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    ##create whatabook_user
    print("Deleting whatabook_user if it exists.")
    cursor.execute("DROP USER IF EXISTS 'whatabook_user'@'localhost';")
    print("Creating whatabook_user.")
    cursor.execute("CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';")
    print("Granting all privileges to whatabook_user.")
    cursor.execute("GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';")

    ##create tables
    print("Deleting tables if they exist.")
    cursor.execute("ALTER TABLE wishlist DROP FOREIGN KEY fk_book;")
    cursor.execute("ALTER TABLE wishlist DROP FOREIGN KEY fk_user;")
    cursor.execute("DROP TABLE IF EXISTS store;")
    cursor.execute("DROP TABLE IF EXISTS book;")
    cursor.execute("DROP TABLE IF EXISTS wishlist;")
    cursor.execute("DROP TABLE IF EXISTS user;")

    print("Creating store table.")
    cursor.execute("CREATE TABLE store ( \
        store_id    INT             NOT NULL    AUTO_INCREMENT, \
        locale      VARCHAR(500)    NOT NULL, \
        PRIMARY KEY(store_id));")

    print("Creating book table.")
    cursor.execute("CREATE TABLE book ( \
    book_id     INT             NOT NULL    AUTO_INCREMENT, \
    book_name   VARCHAR(200)    NOT NULL, \
    author      VARCHAR(200)    NOT NULL, \
    details     VARCHAR(500), \
    PRIMARY KEY(book_id));")

    print("Creating user table.")
    cursor.execute("CREATE TABLE user ( \
    user_id         INT         NOT NULL    AUTO_INCREMENT, \
    first_name      VARCHAR(75) NOT NULL, \
    last_name       VARCHAR(75) NOT NULL, \
    PRIMARY KEY(user_id));")

    print("Creating wishlist table.")
    cursor.execute("CREATE TABLE wishlist ( \
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT, \
    user_id         INT         NOT NULL, \
    book_id         INT         NOT NULL, \
    PRIMARY KEY (wishlist_id), \
    CONSTRAINT fk_book \
    FOREIGN KEY (book_id) \
        REFERENCES book(book_id), \
    CONSTRAINT fk_user \
    FOREIGN KEY (user_id) \
        REFERENCES user(user_Id));")


    print("Inserting store records.")
    cursor.execute("INSERT INTO store(locale) \
        VALUES('406 S. Main St., Laura, OH 45337');")
    
    print("Inserting book records.")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('This is a Book: Volume 1', 'Bob Johnson', 'A brief description about why a good is a book.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('This is a Book: Volume 2', 'Bob Johnson', 'Another stunning depiction of bibliographic works.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('The Search for More', 'Colin Jackson', 'Finding yourself through an examination of history.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('Cooking Shows Make You Eat More!', 'Sally Mae', 'Why do we watch cooking shows if they make us fat?');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('This Book is Also Nonsense', 'Robert Fitzguard III', 'Making up fake book records for a database is just the beginning.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('Nine Records: A Lot of Make Believe', 'Will E Sanders', 'The art of crafting words into sentences that might also mean nothing.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('500 Characters Is Not Enough', 'Eddy Extreme', 'Limits are made to be broken and Eddy Extreme says so.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('What Should Your 8th Record Be?', 'Lammy Unger', 'A far reaching dramatization of the struggles of modern programming.');")
    cursor.execute("INSERT INTO book(book_name, author, details) \
        VALUES('The Final Entry', 'Annie Moss', 'There are lots of books in the world, but this is the last one.');")

    print("Inserting user records.")
    cursor.execute("INSERT INTO user(first_name, last_name) \
        VALUES('Mike', 'Beck');")
    cursor.execute("INSERT INTO user(first_name, last_name) \
        VALUES('Jeff', 'Wolfe');")
    cursor.execute("INSERT INTO user(first_name, last_name) \
        VALUES('Nathaniel', 'Weiser');")

    print("Inserting wishlist records.")
    cursor.execute("INSERT INTO wishlist(user_id, book_id) \
        VALUES ( \
            (SELECT user_id FROM user WHERE first_name = 'Mike'), \
            (SELECT book_id FROM book WHERE book_name = 'Nine Records: A Lot of Make Believe'));")
    cursor.execute("INSERT INTO wishlist(user_id, book_id) \
        VALUES ( \
            (SELECT user_id FROM user WHERE first_name = 'Jeff'), \
            (SELECT book_id FROM book WHERE book_name = 'This is a Book: Volume 1'));")
    cursor.execute("INSERT INTO wishlist(user_id, book_id) \
        VALUES ( \
            (SELECT user_id FROM user WHERE first_name = 'Nathaniel'), \
            (SELECT book_id FROM book WHERE book_name = 'The Final Entry'));")

    input("\n\n Press any key to continue...")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    
    else:
        print(err)
finally:
    db.close()