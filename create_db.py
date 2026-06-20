import sqlite3
conn=sqlite3.connect("patients.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
            code TEXT PRIMARY KEY ,
            name TEXT NOT NULL,
               illness TEXT NOT NULL,
               medication TEXT NON NULL,
               schedule TEXT NOT NULL,
               notes TEXT
)
""")
cursor.execute("""
               INSERT OR REPLACE INTO patients
               VALUES(
               '1001',
               'John Smith',
               'Diabetes',
               'Insulin',
               '08:00 - 20:00',
               'Stable')""")
cursor.execute("""
INSERT OR REPLACE INTO patients
VALUES (
    '1002',
    'Sarah Brown',
    'Asthma',
    'Ventolin',
    '09:00',
    'No allergies'
)
""")

conn.commit()
conn.close()
print("Databse created.")