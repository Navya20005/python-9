class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 15000:
            self.__salary = salary
        else:
            print("Salary should not be less than 15000")
            
    def display_details(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)


employee = Employee("Navya", "IT", 25000)
employee.display_details()
employee.salary = 30000
print("\nAfter Salary Update:")
employee.display_details()
employee.salary = 10000