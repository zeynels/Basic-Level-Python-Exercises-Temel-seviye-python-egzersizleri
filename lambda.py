# def square(num): return num **2
square = lambda num: num **2
numbers =[1,3,5,9,10, 4]

# result = list(map(lambda num: num ** 2, numbers))
# result = list(map(square, numbers))

def check_even(num):    return num %2 == 0

result = list(filter(lambda num: num%2 == 0, numbers))

print(result)