import subprocess
import json
import logging
from severity_scoring import map_bandit_severity

class SecurityChecker:
    def check(self, file_path):
        issues = []
        try:
            # Bandit returns exit code 1 if issues are found
            result = subprocess.run(
                ['bandit', '-f', 'json', '-r', file_path],
                capture_output=True,
                text=True,
                check=False
            )

            if result.stdout:
                try:
                    data = json.loads(result.stdout)
                    # Bandit results are in data['results']
                    for item in data.get('results', []):
                        severity = map_bandit_severity(item.get('issue_severity'))
                        issue = {
                            'tool': 'bandit',
                            'type': 'Security Vulnerability',
                            'description': item.get('issue_text'),
                            'line': item.get('line_number'),
                            'severity': severity,
                            'code': item.get('test_id')
                        }
                        issues.append(issue)
                except json.JSONDecodeError:
                    logging.error("Failed to parse bandit JSON output")
        except Exception as e:
            logging.error(f"Error running bandit: {e}")

        return issues
