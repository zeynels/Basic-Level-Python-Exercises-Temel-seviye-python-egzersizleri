# x = 5

# hak = 0 
# devam = "e"

# # result = 5 < x < 10
# # and 

# # True + True --> True
# # True + False --> False

# # result = (x >5 ) and ( x <10)
# # result = (hak > 0 ) and (devam =="e")


# # or

# # True , False => True
# # True, True => True
# # False, False => False

# result = (x > 0) or  (x%2 == 0)


# #not

# result = not(x > 0)

# result = (x>5) and (x < 10) and (x%2==2)
# print(result)


# sonuc = 0 < a < 100
# print(f" Sayi 0-100 arasinda mi: {})
# sonuc = ( a>0) and (a%2==0)

# sonuc = a < b < c
# email = input("e mail giriniz: ")
# password = input("sifre giriniz: ")

# girilenemail = input("email: ")
# girilenesifre = input("Sifre: ")

# result  = (email == girilenemail) and (password == girilenesifre)

# print(f"E mail dogru: Sifre dogru: {result}")

# a = int(input("Bir sayi giriniz"))
# b = int(input("Bir sayi giriniz"))
# c = int(input("Bir sayi giriniz"))
# result = (a > b ) and (a> c)
# print(f"A en buyuk sayi {result}")
# result = (b>a) and ( b> c)
# print(f"B en buyuk sayi {result}")
# result = (c > b ) and (c> a)
# print(f"c en buyuk sayi {result}")

# vize1 = int(input("İlk vize notunu giriniz: "))
# vize2 = int(input("İkinci vize notunu giriniz: "))
# final = int(input("Final notunu giriniz: "))
# sonuc = ((vize1 + vize2)//2)*0.6 + (final*0.4 )
# gectikaldi = (sonuc > 50) and (final > 50) or (final > 70)
# print(f"Dersi gecme durumu: {gectikaldi}")

isim = input("isim giriniz: ")
kilo = float(input("Kilo giriniz: "))
boy = float(input("Boy giriniz: "))
indeks = (kilo//(boy**2))

zayif = (indeks> 0) and  (indeks <18.4)
normal = (indeks> 18.4) and  (indeks < 24.9)
fazla = (indeks> 25.0 ) and  (indeks < 29.9)
sisman = (indeks> 30) and  (indeks < 34.9)
print(f"İsim: {isim} Durum zayif:  {zayif}" )
print(f"İsim: {isim} Durum normal: {normal}" )
print(f"İsim: {isim} Durum fazla kilolu: {fazla}" )
print(f"İsim: {isim} Durum obez {sisman}")