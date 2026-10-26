from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Hello World!</h1><p>Flask is running inside a Docker container.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
