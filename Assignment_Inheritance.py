#Question 4 (Inheritance)

class Product:
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def display(self):
        print (f"ID no :{self.id}, Name: {self.name}")

class A(Product):
    def __init__(self, id, name, count, category):
        super().__init__(id, name)
        self.count=count
        self.category=category
    def display(self):
        print (f"ID no :{self.id}, Name: {self.name}, Count: {self.count}, category : {self.category}")
class B(Product):
    def __init__(self, id, name, count, category):
        super().__init__(id, name)
        self.count=count
        self.category=category
    def display(self):
        print (f"ID no :{self.id}, Name: {self.name}, Count: {self.count}, category : {self.category}")
class C(Product):
    def __init__(self, id, name, count, category):
        super().__init__(id, name)
        self.count=count
        self.category=category
    def display(self):
        print (f"ID no :{self.id}, Name: {self.name}, Count: {self.count}, category : {self.category}")
    


a= A(37, "Milma", 50, "Butter")
b= B(54, "Milma", 90, "Milk")
c= C(12, "Milma", 56, "Choco")
a.display()
b.display()
c.display()