# Inheritance (Kalıtım): Miras alma
# Person name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)



class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastname = lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a person")
    def eat(self):
        print("I am eating")
    

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentnumber = number
        print('Student Created')
    def who_am_i(self):
        print("I am a student")


class Teacher(Person):

    def __init__(self, fname, lname, branch):      
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")


p1 = Person("Ali", "Yılmaz")
p2 = Student("Ahmet", "Kaya", 1453)
t1 = Teacher("Bahar", "Kahraman", "İngilizce")
t1.who_am_i()

print(f"p1 ad soyad: {p1.firstName} {p1.lastname}")
print(f"Öğrenci ad soyad: {p2.firstName} {p2.lastname} -- Öğrenci no: {p2.studentnumber}")
print(f"Öğrenci ad soyad: {t1.firstName} {t1.lastname} -- Öğretmen branşı {t1.branch}")


# p1.who_am_i()
# p2.who_am_i()

# p1.eat()
# p2.eat()