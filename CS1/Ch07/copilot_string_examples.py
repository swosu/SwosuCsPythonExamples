greeting = "Hello"

print(greeting)
#print(greeting.upper())
#print(dir(greeting))

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")

    def go_to_work(self):
        print(f"{self.name} is going to work")

person = Person("Alice")
print(person)
person.say_hello()
print(dir(person))

class Dog:
    def __init__(self, name):
        self.name = name

bobber = Dog("Bobber")
print(dir(bobber))
