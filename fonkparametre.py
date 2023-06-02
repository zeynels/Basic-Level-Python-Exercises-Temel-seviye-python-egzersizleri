# def changName(n):
#     n = "Ada"

# name = "Yiğit"

# changName(name)
# print(name)

# def change(n):
#     n[0] = "İstanbul"

# sehirler = ["Ankara", "İzmir"]
# n = sehirler[:]

# n[0]: "İstanbul"
# print(sehirler)

# print(n)

# def add(*params):
#     # print(params)
#     # return sum((params))
#     sum = 0
#     for n in params:
#         sum = sum + n
#     return sum

# print(add("Zeynel", 20))
# print(add(10, 20,40))
def displayUser(**params):
    print(type(params))
    for key, value in params.items():
        print("{} is {}".format(key, value))
displayUser(name = "Çınar", age = 2, city = "İstanbul")
displayUser(name = "Ali", age = 25, city = "İzmir", phone ="151781")
displayUser(name = "Yigit", age = 12, city = "İzmir", phone ="254812", email = "yigit@gmail.com")

def myfunc(a,b,*params,**kwargs):
    print(a)
    print(b)
    print(params)
    print(kwargs)

myfunc(10,20,30,40,50, key1 ="value 1", key2 = "value 2")
