import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Example coin data
coins = [
    {"name": "Bitcoin", "confidence": 0.8},
    {"name": "Ethereum", "confidence": 0.75},
    {"name": "Litecoin", "confidence": 0.6},
]

# Indicator info per coin
indicators = {
    c["name"]: {"rsi": random.randint(20, 80), "reversal": False} for c in coins
}

def refresh_data():
    """Update coin scores and indicators with random values."""
    for coin in coins:
        coin["confidence"] = round(random.random(), 2)
        indicators[coin["name"]] = {
            "rsi": random.randint(20, 80),
            "reversal": random.random() > 0.8,
        }

@app.route("/")
def index():
    refresh_data()
    return render_template("index.html", coins=coins, indicators=indicators)

@app.route("/update")
def update():
    refresh_data()
    return jsonify({"coins": coins, "indicators": indicators})

@app.route("/backtest", methods=["POST"])
def backtest():
    coin = request.json.get("coin")
    # Placeholder for running backtests
    message = f"Backtest triggered for {coin}"
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
