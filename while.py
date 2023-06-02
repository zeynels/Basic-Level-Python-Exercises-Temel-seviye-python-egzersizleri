# # x = 0 
# # while x <=  50:
# #      if (x % 2 == 0):
# #       print(x) 
# #      x  += 1 
# name = ""
# while not name:
#     name = input("İsminizi girin: ")

# print(f"Merhaba {name}")


#####################################################################################
                        # Uygulama
#####################################################################################

# sayilar = [1,3,5,7,9,12,19,21]
# i = 0
# while (i < len(sayilar)):
#      print(sayilar[i])
#      i += 1
# i = 0
# bas = int(input("Baslangic degerini giriniz : "))
# son = int(input("Bitis degerini giriniz : "))

# while  i < son:
#     if ( i% 2 == 1):
#       print(i)
  
#     i+=1     

# i = 100
# while 0 <= i:
#     print(i)
#     i-=1

# numbers = []

# i = 0
# while i <5:
#     sayi = (int(input("Sayi: ")))
#     numbers.append(sayi)
#     i+=1

# numbers.sort()
# print(numbers)

i = 0
urunler = []
urunsayi = int(input("Girmek istediginiz urun sayisi: "))
while i < urunsayi:
    urun = {}
    isim = input("Urun ismini giriniz: ")
    urun["name"] = isim
    fiyat = input("Urun fiyatini giriniz: ")
    urun["price"] = fiyat
    urunler.append(urun)
    i +=1


for urun in urunler:
    print(f"Urun adi: {urun['name']}\t Urun fiyati: {urun['price']}")
    
