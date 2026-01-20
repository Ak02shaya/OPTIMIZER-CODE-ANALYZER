import subprocess
import json
import logging
import autopep8
from severity_scoring import map_radon_rank

class OptimizationEngine:
    def analyze(self, file_path):
        issues = []
        optimized_code = ""

        # Check Complexity with Radon
        try:
            result = subprocess.run(
                ['radon', 'cc', '-j', file_path],
                capture_output=True,
                text=True,
                check=False
            )

            if result.stdout:
                try:
                    data = json.loads(result.stdout)
                    # data is dict {filename: [blocks]}
                    for filename, blocks in data.items():
                        for block in blocks:
                            rank = block.get('rank')
                            # Flag C, D, E, F as issues. A and B are usually acceptable.
                            if rank in ['C', 'D', 'E', 'F']:
                                severity = map_radon_rank(rank)
                                issue = {
                                    'tool': 'radon',
                                    'type': 'Performance/Complexity',
                                    'description': f"High Cyclomatic Complexity ({block.get('complexity')}) in {block.get('type')} '{block.get('name')}'",
                                    'line': block.get('lineno'),
                                    'severity': severity,
                                    'code': 'cyclomatic-complexity'
                                }
                                issues.append(issue)
                except json.JSONDecodeError:
                    logging.error("Failed to parse radon JSON output")
        except Exception as e:
            logging.error(f"Error running radon: {e}")

        # Generate Optimized Code (Formatting)
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            optimized_code = autopep8.fix_code(content)
        except Exception as e:
            logging.error(f"Error running autopep8: {e}")

        return issues, optimized_code
