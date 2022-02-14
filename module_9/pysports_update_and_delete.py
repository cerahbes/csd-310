import mysql.connector
from mysql.connector import errorcode

config = {
        "user": "root",
        "password": "sailorV1!isgreat",
        "host": "127.0.0.1",
        "database": "pysports",
        "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute("INSERT INTO player (player_id, first_name, last_name, team_id) \
                        VALUES(21, 'Smeagol', 'Shire Folk', 1);")
    
    join1 = ("SELECT player_id, first_name, last_name, team_name \
            FROM player \
            INNER JOIN team \
                ON player.team_id = team.team_id \
            ORDER BY \
                player_id;")
            
    cursor.execute(join1)

    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    for row in cursor:
            print("Player ID:",(row[0]))
            print("First Name:",(row[1]))
            print("Last Name:",(row[2]))
            print("Team Name:",(row[3]))
            print()

    cursor.execute("UPDATE player \
                    SET team_id = 2, \
                        first_name = 'Gollum', \
                        last_name = 'Ring Stealer' \
                    WHERE first_name = 'Smeagol';")

    cursor.execute(join1)
   
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    for row in cursor:
            print("Player ID:",(row[0]))
            print("First Name:",(row[1]))
            print("Last Name:",(row[2]))
            print("Team Name:",(row[3]))
            print()

    cursor.execute("DELETE FROM player \
                    WHERE first_name = 'Gollum';")
    
    cursor.execute(join1)

    print("-- DISPLAYING PLAYERS AFTER DELETE --")
    for row in cursor:
            print("Player ID:",(row[0]))
            print("First Name:",(row[1]))
            print("Last Name:",(row[2]))
            print("Team Name:",(row[3]))
            print()




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