
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def old(data):
    names = set([])
    for person in data:
        names.add(person.name)
    return names


def new(data):
    """ TODO """
    pass


if __name__ == "__main__":
    data = [Person(name, age) for name, age in
            [("Knut", 30), ("Knut", 29), ("Stine", 30),
             ("Brita", 60), ("Olav", 40)]]
    assert old(data) == new(data)
    print("SUCSESS!")
