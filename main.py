from flask import Flask, render_template
from fetch_img import winter_sales


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_urls=winter_sales())

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
