from flask import Flask, render_template, request, jsonify, session
from getdata import get_images
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    """
    Simple route to home page, renders index.html

    Returns:
        - Render template for index.html, return all images and products
    """
    return render_template("index.html", image_paths=get_images(None))

@app.route('/products')
def products():
    sort = request.args.get('sort')
    category = request.args.get('category')
    image_paths = get_images(category, sort=sort)
    return render_template('products.html', image_paths=image_paths, category=category)    

@app.route('/checkout')
def checkout():
    """
    Route to checkout page, extracts each product that has been added to cart.
    Displays name and price for each product, as well as the quantity.
    Also calculates the total price.

    Returns:
        - Render template for checkout, including every item in the cart and the total price
    """

    cart_items = session.get('cart_items', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)

    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)


@app.route('/products_by_category')
def products_by_category():
    """
    Route to each category button, is used to display products
    by category. Retrieves category name from each button.

    Returns:
        - Render template for products.html file, includes all images with correct category

    """
    category = request.args.get('category')
    return render_template('products.html', image_paths=get_images(category, None))


@app.route('/slider', methods=['POST'])
def handle_slider():
    """
    Extracts slider values from JSON data received via request,
    ensures the minimum and maximum slider values are properly assigned,
    and returns JSON response with corrected slider values.

    Returns:
    - JSON response containing the corrected minimum and maximum slider values.
    - HTTP status code 200 indicating a successful request.

    Notes:
    - Expects JSON data with keys 'minValue' and 'maxValue'.
    - Assigns 'minValue' to slider_value_min and 'maxValue' to slider_value_max.
    """

    data = request.get_json()
    slider_value_min = min(data.get('minValue'), data.get('maxValue'))
    slider_value_max = max(data.get('minValue'), data.get('maxValue'))

    return jsonify({"minValue": slider_value_min, "maxValue": slider_value_max}), 200


if __name__ == "__main__":
    app.run(debug=True)
