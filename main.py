import os

# ... (Keep all your existing model and route code here) ...

if __name__ == "__main__":
    # This line is the "correct" way to handle Render's dynamic port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
