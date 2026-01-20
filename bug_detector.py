import subprocess
import json
import logging
from severity_scoring import map_pylint_category

class BugDetector:
    def detect(self, file_path):
        issues = []
        try:
            # Pylint returns non-zero exit code if issues are found, so check=False is needed.
            result = subprocess.run(
                ['pylint', file_path, '--output-format=json'],
                capture_output=True,
                text=True,
                check=False
            )

            if result.stdout:
                try:
                    data = json.loads(result.stdout)
                    for item in data:
                        # item keys: type, module, obj, line, column, endLine, endColumn, path, symbol, message, message-id
                        severity = map_pylint_category(item.get('type'))
                        issue = {
                            'tool': 'pylint',
                            'type': 'Bug/Code Smell',
                            'description': item.get('message'),
                            'line': item.get('line'),
                            'severity': severity,
                            'code': item.get('symbol') # or message-id
                        }
                        issues.append(issue)
                except json.JSONDecodeError:
                    # Sometimes pylint outputs non-json text if there are config errors, ignoring for now or logging
                    logging.error(f"Failed to parse pylint JSON output. Raw output: {result.stdout[:100]}...")
        except Exception as e:
            logging.error(f"Error running pylint: {e}")

        return issues
