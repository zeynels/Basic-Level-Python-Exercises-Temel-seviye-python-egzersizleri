
# class Person:
#     address = "no information"
#     def __init__(self,name,year):
        
#         self.name = name
#         self.year = year 
#         # print("init metodu çalıştı")
#     def intro(self):
#             return f"Hello there i am " + self.name
#     def calculateage(self):
#          return 2023 - self.year  



# p1 = Person(name = "ali", year=1990)
# p2 = Person(name = "yağmur", year=1995)

# # p1.intro()
# print(f"{p1.intro()}, {p1.calculateage()} yaşındayım")
# p2.intro()
# p1.calculateage()


class circle:
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap
    
    def cevre_hesaplama(self):
        return 2* self.pi * self.yaricap
    
    def alan_hesaplama(self):
        return self.pi * (self.yaricap ** 2)
        


c1 = circle()

c2 = circle(10)

print(f"c1 alan = {c1.alan()}, c1 çevre = {c1.cevre()}")
print(f"c2 alan = {c2.alan()}, c2 çevre = {c2.cevre()}")
