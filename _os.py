import os
import datetime

# result = os.name
# klasör oluşturma
# os.mkdir("klasör")

# dizin değiştirme
# os.chdir('../..')

# etkin dizin öğrenme
# result = os.getcwd()


# iç içe klasör
# os.makedirs("newdirectory/yeniklasör")

# listeleme
# result = os.listdir()

# result = os.listdir("C:/\")

# print(result)


# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)


# result = os.stat("first_app.py")
# # result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)
# print(result)
# os.removedirs("C:/Users/Zeynel/Desktop/Newdirectory/yeniklasör")

# os.system("notepad.exe")

# result = os.path.abspath("class.py")
# result = os.path.dirname("C:/Users/Zeynel/Desktop/okul/python/class.py")
# print(result)

# result = os.path.dirname(os.path.abspath("class.py"))
result = os.path.exists("_os.py")
result = os.path.isdir("_os.py")
result = os.path.isfile("_os.py")

result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")

print(result)



