import mysql.connector
from mysql.connector import errorcode

config = {
        "user": "pysports_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "pysports",
        "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

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

cursor = db.cursor()

print ("-- create pysports_user and grant them all privileges to the pysports database")
cursor.execute("CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';")

print ("-- grant all privileges to the pysports database to user pysports_user on localhost")
cursor.execute("GRANT ALL PRVILEGES ON pysports.* TO 'pysports_user'@'localhost';")

print ("-- drop test user if exists")
cursor.execute("DROP USER IF EXISTS 'pysports_user'@'localhost';")

print ("-- create the team table")
cursor.execute(CREATE TABLE team
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
);

print ("-- create the player table and set the foreign key")
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

print ("-- insert team records")
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');

print ("-- drop tables if they are present")
DROP TABLE IF EXISTS player;

SELECT team_id FROM team WHERE team_name = 'Team Sauron';

