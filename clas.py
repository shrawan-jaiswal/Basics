class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point(10,20)
point1.x = 203
print(point1.x)

point2 = Point()
point2.y = 10
print(point2.y)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi I am {self.name}')


john = Person("john smith")
john.talk()

bob = Person("Bobby lashly")
bob.talk()



#This is the example of inheritance...create parent class like we create class Mammal() here and we use inheritance by
#creating another class like class  Dog(Mammal): this is how we can create inheritance

class Mammal():
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Dog barks")


class Cat(Mammal):
    def annoyed(self):
        print("Cats are annoying")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.annoyed()

dog1.walk()
