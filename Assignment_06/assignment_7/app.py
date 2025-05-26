class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

# Usage
emp = Employee("Usama", 50000, "123-45-6789")

print(emp.name)         # Works fine
print(emp._salary)      # Works, but should be treated as protected
# print(emp.__ssn)      # Error: AttributeError

# Access private variable using name mangling
print(emp._Employee__ssn)  # Works but not recommended
