import sqlite3

def schema(dbpath=""):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS User(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR UNIQUE NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            artist_id VARCHAR UNIQUE NOT NULL,
            top_tracks VARCHAR NOT NULL
             );""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Playlist(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            valence FLOAT,
            daneability FLOAT,
            energy FLOAT,
            name VARCHAR UNIQUE NOT NULL,
            playlist_id VARCHAR UNIQUE NOT NULL,
            user_id VARCHAR UNIQUE NOT NULL,
            );""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Artist(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR UNIQUE NOT NULL,
            artist_id VARCHAR UNIQUE NOT NULL,
            image VARCHAR UNIQUE NOT NULL,
            );""")

schema()
