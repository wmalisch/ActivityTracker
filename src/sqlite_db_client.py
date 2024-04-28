import sqlite3

from datetime import datetime

class SQLiteDBClient:
    def __init__(self, db):
        self.db = db

    def connect(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def insert_activity_entry(self, startdate, starttime, enddate, endtime, steps):

        start_datetime = datetime.strptime(starttime, '%H:%M:%S')
        end_datetime = datetime.strptime(endtime, '%H:%M:%S')

        time_difference = end_datetime - start_datetime

        minutes = (time_difference.seconds // 60) % 60
        seconds = time_difference.seconds % 60
        duration = "{:02d}:{:02d}".format(minutes, seconds)

        self.cursor.execute("INSERT INTO activity (startdate, starttime, enddate, endtime, steps, duration) VALUES (?, ?, ?, ?, ?, ?)",
                            (startdate, starttime, enddate, endtime, steps, duration))
        self.conn.commit()

    def get_latest_activity(self):
        self.cursor.execute("SELECT steps, duration FROM activity ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()
    
    def get_all(self):
        self.cursor.execute("SELECT * FROM activity ORDER BY id DESC")
        return self.cursor.fetchall()