from bug_detector import BugDetector
from security_checker import SecurityChecker
from optimization_engine import OptimizationEngine
import os

class JulesService:
    def __init__(self):
        self.bug_detector = BugDetector()
        self.security_checker = SecurityChecker()
        self.optimization_engine = OptimizationEngine()

    def analyze_code(self, file_path):
        results = {
            'issues': [],
            'optimized_code': "",
            'unit_test_snippet': ""
        }

        # Run Bug Detector
        bug_issues = self.bug_detector.detect(file_path)
        results['issues'].extend(bug_issues)

        # Run Security Checker
        security_issues = self.security_checker.check(file_path)
        results['issues'].extend(security_issues)

        # Run Optimization Engine
        opt_issues, optimized_code = self.optimization_engine.analyze(file_path)
        results['issues'].extend(opt_issues)
        results['optimized_code'] = optimized_code

        # Generate Dummy Unit Test Snippet
        results['unit_test_snippet'] = self._generate_test_snippet(file_path)

        return results

    def _generate_test_snippet(self, file_path):
        filename = os.path.basename(file_path)
        module_name = filename.replace('.py', '')

        return f"""import unittest
import {module_name}

class Test{module_name.capitalize()}(unittest.TestCase):
    def test_example(self):
        # TODO: Write specific tests for {module_name}
        pass

if __name__ == '__main__':
    unittest.main()
"""
