from flask import Flask, render_template, url_for
from views import root, business_pages

app = Flask(__name__)
app.register_blueprint(root)
app.register_blueprint(business_pages)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, Debug=False)
