from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Docker + AWS CI/CD Project</h1>
    <p>Flask application running successfully!</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
