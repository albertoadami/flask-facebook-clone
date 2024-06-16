from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health_check():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)