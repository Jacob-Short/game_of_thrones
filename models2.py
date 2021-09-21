

class Person():

    def __init__(self, first, last, email) -> None:
        self.first = first
        self.last = last
        self.email = email

    def __str__(self) -> str:
        return f'{self.first} {self.last}'



new_person = Person('jacob', 'short', 'jacobshort.stu@gmail.com')
new_person2 = Person('raelynn', 'short', 'rr@gmai.com')

print(new_person)
print(new_person.email)
print(new_person2)