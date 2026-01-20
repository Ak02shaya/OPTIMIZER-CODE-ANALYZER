# Automated Code Review & Bug Detection Tool

This tool provides automated code analysis for Python projects, checking for:
1. Bugs and Code Smells (using Pylint)
2. Security Vulnerabilities (using Bandit)
3. Performance Issues and Complexity (using Radon)

It generates a report with:
- Issue description
- Severity level
- Suggested fix (via static analysis messages)
- Optimized code snippet (via autopep8 formatting)
- Unit test cases (template generation)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:3000`.
3. Upload a Python file (`.py`) to analyze.
4. View the results.

## Project Structure

- `app.py`: Main Flask application.
- `jules_service.py`: Core logic orchestrating analysis tools.
- `bug_detector.py`: Pylint integration.
- `security_checker.py`: Bandit integration.
- `optimization_engine.py`: Radon and Autopep8 integration.
- `upload_routes.py`, `analysis_routes.py`: API endpoints.
- `templates/`: HTML templates.
- `uploads/`: Temporary storage for uploaded files.

## Testing

Run unit tests:
```bash
python -m unittest test_code_analysis.py
```
