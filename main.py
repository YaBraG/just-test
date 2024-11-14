from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # Get the port number from the environment variable or default to 5000
    port = int(os.environ.get("PORT", 5))

    # Print the port number
    print(f"Running on port {port}")

    app.run(debug=False, host='0.0.0.0', port=port)