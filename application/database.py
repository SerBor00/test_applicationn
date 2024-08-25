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
    CREATE TABLE IF NOT EXISTS match_info (
        name_of_team VARCHAR(50) NOT NULL,
        name_of_game VARCHAR(200) NOT NULL,
        date_of_game DATE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS match_players_info (
        first_and_second_name_1 VARCHAR(100) NOT NULL,
        first_and_second_name_2 VARCHAR(100) NOT NULL,
        first_and_second_name_3 VARCHAR(100),
        first_and_second_name_4 VARCHAR(100),
        first_and_second_name_5 VARCHAR(100)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS points (
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
        extra_seven INT,
        extra_eight INT,
        extra_nine INT,
        points INT,
        final_percentage FLOAT

    )
""")

def path_db ():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "sqlite3.db")
    return db_path

def inp_filter(text, *args):
    max_length = 3
    
    if len(text) <= max_length and text in "01234":
        return text
    else:
        return ''