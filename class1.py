#
#
#a method is a function under a class and it is used to perform a specific task and it is called using the object of the class  
class Student:
    def __init__(self , name, age , course):
        self.name = name
        self.age = age
        self.course = course
        
uni = Student("Esike", 18, "Software Engineering") # here we are creating an object of the class Student and passing the values of name, age, and course as arguments to the constructor method __init__ and storing the object in the variable set
result = uni.name
result1 = uni.age
result2 = uni.course
print(result)
print(result1)
print(result2)