class Student:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 <= age <= 60:
            self.__age = age
        else:
            print("Invalid age")
            
student = Student(20)
print("Age:", student.age)
student.age = 25
print("Updated Age:", student.age)
student.age = 65
