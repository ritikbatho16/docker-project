from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask API 🚀"

@app.route('/user')
def get_user():
    return {"id": 1, "name": "Ritik"}

@app.route('/product')
def get_product():
    return {"id": 101, "name": "iPhone 15 Pro", "price": 1499}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)