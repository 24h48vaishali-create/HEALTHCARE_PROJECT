from flask import Flask, send_from_directory
from routes import configure_routes
from admin_routes import configure_admin_routes
import os

app = Flask(__name__)
app.secret_key = "healthcare_secret"

configure_routes(app)
configure_admin_routes(app)

@app.route('/')
def home():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/admin_panel')
def admin_page():
    return send_from_directory(os.getcwd(), 'admin.html')

@app.route('/files/<path:filename>')
def assets(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    app.run(port=3000, debug=True)