import sqlite3

def get_images():
    conn = sqlite3.connect("webshop.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT image FROM Products")
    images = cursor.fetchall()
    image_urls = [img[0] for img in images]
    
    conn.close()
    return image_urls
    
