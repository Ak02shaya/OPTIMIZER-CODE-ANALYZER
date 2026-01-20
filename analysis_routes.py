from flask import Blueprint, request, jsonify, render_template, current_app
from werkzeug.utils import secure_filename
from jules_service import JulesService
import os

analysis_bp = Blueprint('analysis', __name__)
service = JulesService()

@analysis_bp.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Ensure upload folder exists
    upload_folder = current_app.config.get('UPLOAD_FOLDER', 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)

    results = service.analyze_code(filepath)

    return render_template('results.html', results=results, filename=filename)
