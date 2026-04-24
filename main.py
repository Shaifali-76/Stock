import os
from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Stock API is running"}

@app.route('/predict/<ticker>')
def predict(ticker):
    # This replaces your notebook logic
    data = yf.download(ticker, period="1mo")
    current_price = data['Close'].iloc[-1]
    return jsonify({"ticker": ticker, "price": float(current_price)})

if __name__ == "__main__":
    # Render requires this specific port logic
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
