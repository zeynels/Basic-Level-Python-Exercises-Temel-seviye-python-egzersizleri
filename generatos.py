def cube():
   

    for i in range(5):
        yield i ** 3

# iterator = cube()

# iterator = iter(generator)

for i in cube:
    print(i)