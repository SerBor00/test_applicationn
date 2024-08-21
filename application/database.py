import sqlite3
import os

conn = sqlite3.connect("application/sqlite3.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        first_and_second_name VARCHAR(100) NOT NULL PRIMARY KEY,
        date_of_born DATE NOT NULL,
        gender VARCHAR(9) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS mixed_doubles (
        name_of_game VARCHAR(100) NOT NULL,
        date_of_game DATE NOT NULL,
        name_of_team VARCHAR(50) NOT NULL,
        first_and_second_name VARCHAR(100) NOT NULL,
        one INT,
        two INT,
        three INT,
        four INT,
        five INT,
        six INT,
        seven INT,
        eight INT,
        nine INT,
        one_zero INT,
        one_one INT,
        one_two INT,
        one_three INT,
        one_four INT,
        one_five INT,
        one_six INT,
        one_seven INT,
        one_eight INT,
        one_nine INT,
        two_zero INT,
        two_one INT,
        two_two INT,
        two_three INT,
        two_four INT,
        two_five INT,
        two_six INT,
        two_seven INT,
        two_eight INT,
        two_nine INT,
        three_zero INT,
        extra_one INT,
        extra_two INT,
        extra_three INT,
        extra_four INT,
        extra_five INT,
        extra_six INT,
        points INT,
        final_percentage INT,

        CONSTRAINT mixed_doubles_referens FOREIGN KEY (first_and_second_name) REFERENCES players (first_and_second_name)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS comands (
        name_of_game VARCHAR(100) NOT NULL,
        date_of_game DATE NOT NULL,
        discipline VARCHAR(30) NOT NULL,
        name_of_team VARCHAR(50) NOT NULL,
        first_and_second_name VARCHAR(100) NOT NULL,
        one INT,
        two INT,
        three INT,
        four INT,
        five INT,
        six INT,
        seven INT,
        eight INT,
        nine INT,
        one_zero INT,
        one_one INT,
        one_two INT,
        one_three INT,
        one_four INT,
        one_five INT,
        one_six INT,
        one_seven INT,
        one_eight INT,
        one_nine INT,
        two_zero INT,
        extra_one INT,
        extra_two INT,
        extra_three INT,
        extra_four INT,
        extra_five INT,
        extra_six INT,
        points INT,
        final_percentage INT,

        CONSTRAINT comands_referens FOREIGN KEY (first_and_second_name) REFERENCES players (first_and_second_name)
        )
""")

conn.commit()
conn.close()

def path_db ():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "sqlite3.db")
    return db_path