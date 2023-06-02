

# mylist = [1,2,3]

# mystring ="my string"

# print(len(mylist))
# print(len(mystring))


class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu')

    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("Film silindi")
m = Movie("Beş şehir", "Onur Ünlü", 100)

# print(len(m))

print(str(m))

print(len(m))

del m