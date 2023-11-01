class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

name = input('Your Name: ')
age = int(input('Age: '))
sex = input('Your Gender: ')
person = Person(name, age, sex)
print(person.name,age,sex)