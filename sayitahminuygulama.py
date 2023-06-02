
# import random
# cevap = random.randint(1,100)
# print(cevap)
# sayac = int(input("Kac caniniz olmasi gerektigini belirleyin"))
# olasi = []
# olasi = range(1,100)
# x = int(input("Bir sayi giriniz: "))
# for x in olasi:
    
# import random

# max_hak = int(input("Kaç hak istersiniz? "))
# sayi_listesi = []

# # Rastgele bir sayı seçin
# tahmin_edilecek_sayi = random.randint(1, 100)

# while len(sayi_listesi) < max_hak:
#     try:
#         # Kullanıcıdan bir sayı isteyin
#         tahmin = int(input("Tahmininiz nedir? (1-100 arası bir sayı girin): "))
#     except ValueError:
#         print("Lütfen bir sayı girin.")
#         continue
    
#     # Sayı 1-100 arasında mı kontrol edin
#     if tahmin < 1 or tahmin > 100:
#         print("Lütfen 1 ile 100 arasında bir sayı girin.")
#         continue
    
#     # Sayı daha önce girildi mi kontrol edin
#     if tahmin in sayi_listesi:
#         print("Bu sayıyı daha önce girdiniz. Lütfen farklı bir sayı girin.")
#         continue
    
#     # Tahmini doğru mu kontrol edin
#     if tahmin == tahmin_edilecek_sayi:
#         print("Tebrikler, doğru tahmin!")
#         break
#     elif tahmin < tahmin_edilecek_sayi:
#         print("Daha yüksek bir sayı girin.")
#     else:
#         print("Daha düşük bir sayı girin.")
    
#     # Kullanıcının girdiği sayıyı sayı listesine ekleyin
#     sayi_listesi.append(tahmin)

# if len(sayi_listesi) == max_hak:
#     print("Hakkınız bitti. Doğru sayı {} idi.".format(tahmin_edilecek_sayi))

import random
sayi = random.randint(1,100)
print(sayi)
can = int(input("Kac hak istersiniz?"))
hak = can
sayac = 0
while hak > 0:
    sayac +=1
    hak -=1
    tahmin = (int(input("Tahmininizi giriniz: ")))

    if sayi == tahmin: 
        print(f"Tebrikler {sayac}. defada bildiniz.\nToplam puanınız: {100 - (100/can)*sayac-1} ")
        break
    elif sayi > tahmin:
        print("Daha buyuk bir sayi giriniz")

    elif tahmin > sayi:
        print("Daha dusuk bir sayi giriniz")
    
    if hak == 0:
        print(f"Hakkiniz bitti.\nDogru cevap:{sayi} ")
