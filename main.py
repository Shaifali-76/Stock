import os
import yfinance as yf
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Stock API is Running!"

@app.route('/predict/<ticker>')
def predict(ticker):
    try:
        # This is where your .ipynb logic goes
        # Example: Fetching the last 5 days of data
        data = yf.download(ticker, period="5d")
        latest_price = data['Close'].iloc[-1]
        
        # Add your specific prediction logic here
        prediction = latest_price * 1.02 # Example: simple 2% growth guess
        
        return jsonify({
            "ticker": ticker,
            "current_price": round(latest_price, 2),
            "prediction": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Crucial for Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
