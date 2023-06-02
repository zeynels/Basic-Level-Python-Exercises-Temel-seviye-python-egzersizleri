

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("y için 0 girilemez")

# except ValueError:
#     print("Lütfen sayısal bir değer giriniz")



# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError)as e:
#     print("Yanlış bilgi girdiniz")
#     print(e)

while True:

    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Yanlış bilgi girdiniz: ", ex)

    else:
        break
    finally:
        print("Try except sonlandı")