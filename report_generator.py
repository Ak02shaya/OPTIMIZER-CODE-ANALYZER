import json

class ReportGenerator:
    @staticmethod
    def generate_json(results):
        return json.dumps(results, indent=4)
