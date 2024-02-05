import sqlite3

def get_images(category):
    conn = sqlite3.connect("webshop.db")
    cursor = conn.cursor()
    
    if category:
        cursor.execute("SELECT name, price, image FROM Products WHERE category = ?", (category,))
    else:
        cursor.execute("SELECT name, price, image FROM Products")

    images = cursor.fetchall()
    image_urls =  [(img[0], img[1], img[2]) for img in images]
    conn.close()
    return image_urls
