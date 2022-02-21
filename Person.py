from enum import Enum
import uuid
import Util

class Person:
    id = None
    lastname = None
    name = None
    age = None
    
    def __init__(self, id, lastname="", name="", age=""):
        self.id = id or uuid.uuid4()
        self.lastname = lastname
        self.name = name
        self.age = age

    def deserialize(line, separator=";"):
        a = line.split(separator)
        return Person(a[1], a[2], a[3], a[4])

    def serialize(self, separator=";"):
        return str(self.__class__.__name__) + separator + str(self.id) + separator + self.lastname + separator + self.name + separator + str(self.age)

    def __repr__(self):
        return self.serialize()

    def __eq__(self, person):
        return str(self.id) == str(person.id)

if __name__ == "__main__":
    p1 = Person(None, "Vidalies", "Mathieu", 42)
    p2 = Person(None, "Vidalies", "Julie", 10)
    p3 = Person(None, "Vidalies")

    for p in [p1, p2, p3]:
        print(p)
        assert(Person.deserialize(p.serialize()).serialize() == p.serialize())
        assert(Person.deserialize(p.serialize()) == p)


