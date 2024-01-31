from flask import Flask, render_template, request, jsonify
from fetch_img import winter_sales


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_urls=winter_sales())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/slider', methods=['POST'])

def handle_slider():
    data = request.get_json()
    slider_value = data['sliderValue']
    print(slider_value)
    
    return slider_value

if __name__ == "__main__":
    app.run(debug=True)
