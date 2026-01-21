from flask import Flask, render_template
from upload_routes import upload_bp
from analysis_routes import analysis_bp
import os

app = Flask(__name__, template_folder='.', static_folder='.')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'supersecretkey'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

app.register_blueprint(upload_bp)
app.register_blueprint(analysis_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
