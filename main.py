from flask import Flask, render_template, request, jsonify, session
from getdata import get_images


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_paths=get_images(None))

# @app.route('/checkout')
# def checkout():
#     return render_template('checkout.html', image_paths=get_images(None))
app.secret_key = 'your_secret_key'  # Needed to use sessions

@app.route('/checkout')
def checkout():
    # Assuming cart items are stored in session['cart_items']
    # Example format: [{'name': 'Product 1', 'price': 10, 'quantity': 1}, ...]
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
    slider_value = data['sliderValue']
    print(slider_value)
    
    return slider_value

if __name__ == "__main__":
    app.run(debug=True)
