# def my_decorator(func):
#     def wrapper():
#         print("Fonksiyondan önceki işlemler")
#         func()
#         print("fonksiyondan sonraki işlemler")
#     return wrapper
# @my_decorator

# def sayHello():
#     print("hello")


# def sayGreeting():
#     print("greeting")

# # sayHello = my_decorator(sayHello)

# sayHello()


import math 
import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon"+str(finish-start))
    return inner


@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
   
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
    


usalma(2,3)
faktoriyel(5)