# import sqlite3

# class db:

#     def __init__(self):
#         self.conn = sqlite3.connect('database.db')
#         self.cur = self.conn.cursor()

#     def __create_companies_table(self):
#         self.cur.execute("CREATE TABLE IF NOT EXISTS companies (id INTEGER PRIMARY KEY, name TEXT NOT NULL, ticker TEXT NOT NULL, naics TEXT NOT NULL)")
#         self.conn.commit()

#     def __create_reports_table(self):
#         self.cur.execute("CREATE TABLE IF NOT EXISTS reports (title TEXT PRIMARY KEY, content TEXT NOT NULL, ticker TEXT NOT NULL, date TEXT NOT NULL)")
#         self.conn.commit()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
