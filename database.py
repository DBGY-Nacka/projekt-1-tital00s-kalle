import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Products (
    productid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    inventory_count INTEGER NOT NULL,
    color TEXT,
    category TEXT NOT NULL,
    rating INTEGER,
)
""")

conn.commit()
conn.close()
 