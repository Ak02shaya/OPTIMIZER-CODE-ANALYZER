class Severity:
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

def map_pylint_category(category):
    if category in ['error', 'fatal']:
        return Severity.HIGH
    elif category == 'warning':
        return Severity.MEDIUM
    else:
        return Severity.LOW

def map_bandit_severity(severity):
    if severity == 'HIGH':
        return Severity.HIGH
    elif severity == 'MEDIUM':
        return Severity.MEDIUM
    else:
        return Severity.LOW

def map_radon_rank(rank):
    if rank in ['F', 'E']:
        return Severity.HIGH
    elif rank in ['D', 'C']:
        return Severity.MEDIUM
    else:
        return Severity.LOW
