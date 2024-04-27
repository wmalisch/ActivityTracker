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
        self.cursor.execute("INSERT INTO activitybasic (startdate, starttime, enddate, endtime, steps) VALUES (?, ?, ?, ?, ?)",
                            (startdate, starttime, enddate, endtime, steps))
        self.conn.commit()

    def update_activity_entry(self, id, enddate, endtime, steps):
        self.cursor.execute("UPDATE activitybasic SET enddate = ?, endtime = ?, steps = ? WHERE id = ?",
                            (enddate, endtime, steps, id))
        self.conn.commit()
