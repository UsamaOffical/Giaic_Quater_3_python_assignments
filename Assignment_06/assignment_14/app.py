class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation (reference)

# Usage
emp = Employee("Ahmed")
dept = Department("IT", emp)
print(f"Department: {dept.name}, Employee: {dept.employee.name}")
