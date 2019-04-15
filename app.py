from flask import Flask, jsonify
import random

from quotes import entrepreneur_quotes

app = Flask(__name__)

@app.route('/api/quotes')
def serve_entrepreneur_quote():
    quotes = entrepreneur_quotes()
    number_of_quotes = len(quotes)
    selected_quote = quotes[random.randint(0, number_of_quotes - 1)]
    return jsonify(selected_quote)

if __name__ == "__main__":
    app.run(debug=True)