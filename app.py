from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    hotels = [
        {"name": "Luxury Hotel", "price": 120},
        {"name": "Beach Resort", "price": 90},
        {"name": "City Hotel", "price": 70}
    ]
    return render_template("game_web.html", hotels=hotels)

if __name__ == "__main__":
    app.run(debug=True)
