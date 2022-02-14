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

    join1 = ("SELECT player_id, first_name, last_name, team_name \
            FROM player \
            INNER JOIN team \
                ON player.team_id = team.team_id;")
            
    cursor.execute(join1)

    print("-- DISPLAYING PLAYER RECORDS --")
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
