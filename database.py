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
    3,  # productid
    'Jeans',  # name
    'These jeans fit any occasion and are a perfect addition to your wardrobe',  # description
    29.99,  # price
    62,  # inventory_count
    'Blue',  # color
    'Clothes',  # category
    4,  # rating    
    "images\jeans.jpg" #image path
)

cursor.execute("""
INSERT INTO Products (productid, name, description, price, inventory_count, color, category, rating, image)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", product_data)

conn.commit()
conn.close()
 