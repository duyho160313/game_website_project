import csv

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("Homepage.html")

@app.route("/game_web")
def game_web():
    return render_template("game_web.html")

@app.route("/hotel")
def hotel_screen():
    hotels = [
        {"name": "Luxury Hotel", "price": 120},
        {"name": "Beach Resort", "price": 90},
        {"name": "City Hotel", "price": 70}
    ]
    return render_template('hotel_screen.html', hotels=hotels)

@app.route('/new')
def new_screen():
    """Renders the destination page."""
    return render_template('new_screen.html')
@app.route('/homework')
def homework():
    """Renders the destination page."""
    return render_template('homework.html')
@app.route('/sign_up')
def sign_up():
    return render_template("signup_web.html")
@app.route("/quiz")
def math_quiz():
    return render_template("Quiz_game.html")


if __name__ == "__main__":
    app.run(debug=True)

