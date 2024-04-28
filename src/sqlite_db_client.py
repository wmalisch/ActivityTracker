import datetime
import sqlite3

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
        duration = time_difference.strftime('%M:%S')

        self.cursor.execute("INSERT INTO activity (startdate, starttime, enddate, endtime, steps) VALUES (?, ?, ?, ?, ?, ?)",
                            (startdate, starttime, enddate, endtime, steps, duration))
        self.conn.commit()

    def get_latest_activity(self):
        self.cursor.execute("SELECT * FROM activity ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()