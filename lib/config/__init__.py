import sqlite3

CONN = sqlite3.connect('lib/db/hospital.db')
CURSOR = CONN.cursor()
