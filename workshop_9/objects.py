class Person:
    def __init__(self, name, last_name, age) -> None:
        # constructor
        self.name = name
        self.last_name = last_name
        if age < 0:
            raise ValueError(f"Age can't be negative. You set it to {age}")
        self.age = age

    def full_name(self):
        return f"{self.name} {self.last_name}"

    def description(self):
        return f"{self.full_name()} is {self.age} years old."

people = [
    Person("John", "Doe", 30), # instance / object of a Person class
    Person("Jane", "Doe", 25),
    Person("Jim", "Doe", 35),
    Person("Jill", "Doe", 40),
    Person("Jack", "Doe", 45),
]

people[0].name = "Johnathan"
# Don't do this
# people[0].pet = "Dog"
# print(people[0].pet)

for person in people:
    # print(person.full_name())
    print(person.description())
    # print(person.pet)
