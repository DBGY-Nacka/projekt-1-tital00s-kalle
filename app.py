from flask import Flask, render_template, request, jsonify, session
from getdata import get_images


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_paths=get_images(None))

app.secret_key = 'your_secret_key'

@app.route('/checkout')
def checkout():

    cart_items = session.get('cart_items', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

@app.route('/products')
def products():
    category = request.args.get('category')
    return render_template('products.html', image_paths=get_images(category))

@app.route('/slider', methods=['POST'])


# Tänk igenom denna funktion. Ska det vara en slider med två värden, eller två sliders
# med varsitt värde? Gör om docstringen efter det.
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
