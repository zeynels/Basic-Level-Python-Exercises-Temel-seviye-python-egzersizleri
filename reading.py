# try:

#     file = open("newfile2.txt","r")
#     print(file)


# except FileNotFoundError:
#      print("Dosya okuma hatası")

# finally:
#      print("dosya kapandı")
#      file.close()


file = open("newfile.txt","r",encoding= "utf-8")


# for i in file:
#     print(i,end="")


# content1 = file.read()
# print("içerik 1")

# print(content1)

# content2 = file.read()
# print("içerik 2")
# file.close()

# content = file.read(5)
# print(content)

# file.close()

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

liste = file.readlines()

print(liste)