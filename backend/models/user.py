import sqlite3

class User:

    dbpath = ""

    def __init__(self, username, email, artist_id, top_tracks, pk=None)
        self.pk = pk
        self.username = username
        self.email = email
        self.artist_id = artist_id
        self.top_tracks = top_tracks


    def insert(self):
        """Add a new account to the database
        """
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO User (username, email, artist_id, top tracks) VALUES (?, ?, ?, ?)"""
            print(sql)
            cursor.execute(sql, [self.username, self.email, self.artist_id, self.top_tracks])