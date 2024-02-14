import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE Products (
#     productid INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     description TEXT,
#     price REAL NOT NULL,
#     inventory_count INTEGER NOT NULL,
#     color TEXT,
#     category TEXT NOT NULL,
#     rating INTEGER,
#     image TEXT
# )
# """)

product_data = (
    6,  # productid
    'Boots',  # name
    'This is a sturdy pair of boots for a person ready for an adventure',  # description
    49.99,  # price
    189,  # inventory_count
    'Black',  # color
    'Clothes',  # category
    5,  # rating    
    "static/images/boots.jpg" #image path
)


conn.commit()
conn.close()
 