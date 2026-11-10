from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask GitOps Demo</title>
        </head>
        <body>
            <h1>Hello from Flask!</h1>
            <h2>Version 1.0</h2>
            <p>Deployed using GitHub Actions and Argo CD.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "flask-gitops-demo",
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)