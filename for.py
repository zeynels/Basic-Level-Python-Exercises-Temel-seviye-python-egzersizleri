# numbers = [1,2,3,4,5]

# for num in numbers:
#     print(num)

# names = ["cınar", "sadık", "sena"]

# for name in names:
#     print(f"My name is {name}")


# name = "Sadık Turan"

# for n in name:
#     print(n)


# tuple = (1,2,3,4,5)

# for t in tuple:
#     print(t)

# d  = {"k1": 1, "k2": 2, "k3":3}

# for key,value in d.items():
#         print(f"Anahtar: {key}\nValue: {value}")


##############################################################

# sayilar = [1,3,5,7,9,12,19,21]

# for a in sayilar:
#     if (a%3 == 0):
#          print(a)
# toplam = 0
# sonuc = int()
# for sayi in sayilar:
#     toplam  = sayi
#     sonuc += toplam
# print(sonuc)

##############################################################

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi

# print(toplam)

##############################################################


# kare = 0
# for sayi in sayilar:
#     if (sayi%2== 1):
#          kare = sayi**2
#          print(kare) 

##############################################################

# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# for sehir in sehirler:
    
#     if (len(sehir) <= 5):
#          print(sehir)

##############################################################
# toplam = 0
# urunler = [
#   {'name':'samsung S6', 'price': '3000' },
#   {'name':'samsung S7', 'price': '4000' },
#   {'name':'samsung S8', 'price': '5000' },
#   {'name':'samsung S9', 'price': '6000' },
#   {'name':'samsung S10', 'price': '7000' }
# ]


# # for urun in urunler:
# #     fiyat = int(urun["price"])
# #     toplam += fiyat

# # print(toplam)

# for urun in urunler:
#      if   int(urun["price"]) <= 5000:
#         print(urun["name"])
         
# sayilar = [1,3,5,7,9,12,19,21]
# for sayi in sayilar:
#     if sayi % 3 == 0:
#       print(sayi)
# sonuc = 0
# sayi = 0
# for sayi in sayilar:
#     sonuc +=sayi
#     print(sonuc)
# for sayi in sayilar:
#     if sayi % 2 == 1:
#         sonuc = sayi*sayi 
#         print(sonuc)
#         sonuc = 0

# sehirler = ["Kocaeli", "İstanbul", "Ankara","İzmir","Rize"]

# for sehir in sehirler:
#     if len(sehir) == 5:
#         print(sehir)
urunler  = [  
    {"name":"samsung s6", "price" : "3000"},
    {'name':'samsung s7', 'price':'4000'},
    {'name':'samsung s8', 'price' :'5000'},
    {'name':'samsung s9', 'price' :'6000'},
    {'name':'samsung s10', 'price' :'7000'}
]
# toplam = 0
# for urun in urunler:
#     fiyat = urun['price']
#     toplam += int(fiyat)
# print(toplam)
for urun in urunler:
    if (int(urun["price"])) < 5000:
        print(urun["name"])