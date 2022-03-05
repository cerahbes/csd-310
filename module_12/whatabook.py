## Title: whatabook.py
## Author: Roben Johnson
## Date 3/5/22
## Description: WhatABook final project

## import statements
import sys
import mysql.connector
from mysql.connector import errorcode

##config for cursor
config = {
        "user": "whatabook_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "whatabook",
        "raise_on_warnings": True
}

##main menu
def main_menu():
    print()
    print(" -- Main Menu -- ")
    print("   1. View Books \n   2. View Store Locations \n   3. My Account \n   4. Exit Program")

    try:
        selection = int(input('   Enter the number to take that action: '))
        return selection
    except ValueError:
        print("\n Invalid selection, exiting program.")
        sys.exit(0)

##menu selection methods
def view_books(cursor): #view books method
    cursor.execute("SELECT book_id, book_name, author, details from book;")
    books = cursor.fetchall()
    print("\n -- BOOKS --")
    for book in books:
        print("   Book Name: {}\n   Author: {}\n   Details: {}\n".format(book[0], book[1], book[2]))

def view_stores(cursor): #view stores method
    cursor.execute("SELECT store_id, locale from store;")
    stores = cursor.fetchall()
    print("\n  -- STORE LOCATIONS --")
    for store in stores:
        print("  Locale: {}\n".format(store[1]))

def  my_account(): #user account validation method
    try:
        user_id = int(input('\n   Enter your user id number: '))
        if user_id < 0 or user_id > 3:
            print("\n Invalid user id, exiting program.")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n Invalid selection, exiting program.")
        sys.exit(0)

def user_wishlist_menu(): #user wishlist menu
    try:
        print("\n   -- Wishlist Menu -- ")
        print("   1. Wishlist \n   2. Add Book \n   3. Remove Book \n   4. Main Menu")
        wish_selection = int(input('   Enter the number to take that action: '))
        return wish_selection
    except ValueError:
        print("\n Invalid selection, exiting program.")
        sys.exit(0)

def show_wishlist(cursor, user_id): #view user wishlist method
    cursor.execute("SELECT user.user_id, user.first_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {};".format(user_id))
    wishlist = cursor.fetchall()
    print("\n   -- WISHLIST -- ")
    for book in wishlist:
        print("   Book Name: {}\n   Author: {}\n".format(book[3], book[4]))

def show_books(cursor, user_id): ##show books to add to user wishlist method
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {});".format(user_id))
    print(query)
    cursor.execute(query)
    show_for_wishlist = cursor.fetchall()
    print("\n   -- BOOKS -- ")
    for book in show_for_wishlist:
        print("   Book Id: {}\n   Book Name: {}\n".format(book[0], book[1]))

def book_to_wishlist(cursor, user_id, book_id): ##add book to wishlist
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {});".format(user_id, book_id))

def remove_wishlist(cursor, user_id): #view user wishlist method
    cursor.execute("SELECT user.user_id, user.first_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN user ON wishlist.user_id = user.user_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE user.user_id = {};".format(user_id))
    wishlist = cursor.fetchall()
    print("\n   -- WISHLIST -- ")
    for book in wishlist:
        print("   Book Id: {}\n   Book Name: {}\n   Author: {}\n".format(book[2], book[3], book[4]))

def remove_wishlist_book(cursor, user_id, book_id):  ##remove book from wishlist
    cursor.execute("DELETE FROM wishlist WHERE user_id = {} AND book_id = {};".format(user_id, book_id))

##main program
try: 
    db = mysql.connector.connect(**config) #connection to database
    cursor = db.cursor() #cursor method to execute SQL commands

    print("\n   *** WhatABook Application ***   ")
    user_selection = main_menu()

    while user_selection != 4:
        if user_selection == 1:
            view_books(cursor)
        if user_selection == 2:
            view_stores(cursor)
        if user_selection == 3:
            my_user_id = my_account()
            account_option = user_wishlist_menu()
            while account_option != 4:
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                if account_option == 2:
                    show_books(cursor, my_user_id)
                    book_id = int(input("\n   Enter the id of the book you want to add to your wishlist: "))
                    book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit()
                    print("\n   Book id: {} has been added to your wishlist.".format(book_id))
                if account_option == 3:
                    remove_wishlist(cursor, my_user_id)
                    book_id = int(input("\n   Enter the id of the book you want to remove from your wishlist: "))
                    remove_wishlist_book(cursor, my_user_id, book_id)
                    db.commit()
                if account_option < 0 or account_option > 4:
                    print("\n   Invalid number, please try again.")
                account_option = user_wishlist_menu()
        if user_selection < 0 or user_selection > 4:
                print("\n   Invalid number, please try again.")
        user_selection = main_menu()

    print("\n Exiting program.")
    
#error handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist.")
    else:
        print(err)

#close connection to database
finally:
    db.close()