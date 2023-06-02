
class Person:
    address = "no information"
    def __init__(self,name,year):
        address = "no information"
        self.name = name
        self.year = year 
        print("init metodu çalıştı")
    def intro(self):
            print("Hello there " + self.name)
        


        
p1 = Person(name = "ali", year=1990)
p2 = Person(name = "yağmur", year=1995)

p1.intro()
# p1.name ="Ahmet"
# p1.address="Kocaeli"

# print(f"p1-->name {p1.name} year: {p1.name} address: {p1.address}")
# print(f"p2-->name {p2.name} year: {p2.name} address: {p2.address}")

