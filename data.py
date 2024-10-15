# data.py
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class PerformanceReview:
    def __init__(self, employee, score, comments):
        self.employee = employee
        self.score = score
        self.comments = comments
