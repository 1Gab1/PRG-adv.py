#question 1:

class Employee:
    def __init__(self, salary):
        self.__salary = salary  # private attribute

    # getter method
    def get_salary(self):
        return self.__salary

    # setter method
    def set_salary(self, amount):
        self.__salary = amount

# create object
emp = Employee(50000)

# access with getter/setter
print("Salary:", emp.get_salary())
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())

#question 2:

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

obj = C()
obj.greet()  # calls A’s greet() because A is listed first

#question 3:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

# create objects
c = Circle(5)
s = Square(4)

print("Circle Area:", c.area())
print("Square Area:", s.area())


#question 4:

class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

# create objects
a = Counter()
b = Counter()
c = Counter()

print("Number of instances:", Counter.count)


