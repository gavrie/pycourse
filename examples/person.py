class Person(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Person {}>".format(self.name)

    def __str__(self):
        return "A person named {}".format(self.name)

p = Person("Moshe")

print p
