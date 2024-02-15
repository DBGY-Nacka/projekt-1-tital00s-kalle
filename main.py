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

def handle_slider():
    data = request.get_json()
    slider_value_min = data.get('minValue')
    slider_value_max = data.get('maxValue')

    print(f"Min Slider Value: {slider_value_min}, Max Slider Value: {slider_value_max}")
    
    return jsonify({"minValue": slider_value_min, "maxValue": slider_value_max}), 200


if __name__ == "__main__":
    app.run(debug=True)
