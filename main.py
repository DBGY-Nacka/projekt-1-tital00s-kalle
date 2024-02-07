from flask import Flask, render_template, request, jsonify
from getdata import get_images


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_paths=get_images(None))

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
