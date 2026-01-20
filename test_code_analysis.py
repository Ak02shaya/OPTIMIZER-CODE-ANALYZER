import unittest
import os
from bug_detector import BugDetector
from security_checker import SecurityChecker
from optimization_engine import OptimizationEngine

class TestCodeAnalysis(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file_temp.py'
        with open(self.test_file, 'w') as f:
            f.write("import os\n\ndef foo():\n    pass\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_bug_detector(self):
        detector = BugDetector()
        issues = detector.detect(self.test_file)
        self.assertIsInstance(issues, list)
        # Should detect unused import
        self.assertTrue(any(i['code'] == 'unused-import' for i in issues))

    def test_security_checker(self):
        checker = SecurityChecker()
        # Create insecure file
        with open('insecure.py', 'w') as f:
            f.write("eval('print(1)')")

        issues = checker.check('insecure.py')
        self.assertTrue(any(i['code'] == 'B307' for i in issues)) # B307 is eval
        os.remove('insecure.py')

    def test_optimization_engine(self):
        engine = OptimizationEngine()
        issues, code = engine.analyze(self.test_file)
        self.assertIsInstance(issues, list)
        self.assertIsInstance(code, str)
        # Check if code is formatted (autopep8 adds 2 lines before func)
        self.assertIn('def foo():', code)

if __name__ == '__main__':
    unittest.main()
