
class Corp(object):
    people = []
    def add(self, name, salary):
        Corp.people.append({ 'name': name, 'salary' : salary})

    def total(self):
        self.total = sum(n['salary'] for n in Corp.people)
        return self.total

c = Corp()
c.add("Foo", 19)
print(c.total())

c.add("Bar", 23)
print(c.total())
