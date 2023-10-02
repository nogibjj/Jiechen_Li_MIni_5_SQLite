"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the spotify_2023_1.db table"""
    conn = sqlite3.connect("spotify_2023_1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM spotify LIMIT 5")
    print("Top 5 rows of the spotify table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"