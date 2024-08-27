import sqlite3
import os

conn = sqlite3.connect("application/sqlite3.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_and_second_name TEXT NOT NULL,
    date_of_born DATE NOT NULL,
    gender TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_of_game TEXT NOT NULL,
    date_of_game DATE NOT NULL,
    name_of_team TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS match_players (
    match_id INTEGER,
    player_id INTEGER,
    PRIMARY KEY (match_id, player_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
    )         
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS points (
    points_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    one INTEGER,
    two INTEGER,
    three INTEGER,
    four INTEGER,
    five INTEGER,
    six INTEGER,
    seven INTEGER,
    eight INTEGER,
    nine INTEGER,
    ten INTEGER,
    eleven INTEGER,
    twelve INTEGER,
    thirteen INTEGER,
    fourteen INTEGER,
    fifteen INTEGER,
    sixteen INTEGER,
    seventeen INTEGER,
    eighteen INTEGER,
    nineteen INTEGER,
    twenty INTEGER,
    twenty_one INTEGER,
    twenty_two INTEGER,
    twenty_three INTEGER,
    twenty_four INTEGER,
    twenty_five INTEGER,
    twenty_six INTEGER,
    twenty_seven INTEGER,
    twenty_eight INTEGER,
    twenty_nine INTEGER,
    thirty INTEGER,
    extra_one INTEGER,
    extra_two INTEGER,
    extra_three INTEGER,
    extra_four INTEGER,
    extra_five INTEGER,
    extra_six INTEGER,
    extra_seven INTEGER,
    extra_eight INTEGER,
    extra_nine INTEGER,
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
    )       
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS match_stats (
    match_id INTEGER,
    points_id INTEGER,
    PRIMARY KEY (match_id, points_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (points_id) REFERENCES points(points_id)
    )         
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS match_persteges_info (
    points_id INTEGER,
    guard_persent REAL,
    dro_persent REAL,
    take_persent REAL,
    final_persent REAL,
    end_1_persent REAL,
    end_2_persent REAL,
    end_3_persent REAL,
    end_4_persent REAL,
    end_5_persent REAL,
    end_6_persent REAL,
    end_7_persent REAL,
    end_8_persent REAL,
    end_9_persent REAL,
    end_10_persent REAL,
    ex_1_end_persent REAL,
    ex_2_end_persent REAL,
    ex_3_end_persent REAL,
    FOREIGN KEY (points_id) REFERENCES points(points_id)
    )        
""")

def path_db ():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "sqlite3.db")
    return db_path

def inp_filter(text, *args):
    if text in "01234":
        return text
    else:
        return ''