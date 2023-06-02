# def tekra(kelime, n):
#     print(kelime * n)

# tekra("Merhaba", 10)


# def listeyeCevir(*args):
#     liste = []
    
#     for arg in args:
#         liste.append(arg)
#     return liste

# result = listeyeCevir(10,20,30,"Merhaba",)
# print(result)

# sayi1 = int(input("ilk sayiyi giriniz: "))
# sayi2 = int(input("İkinci sayiyi giriniz: "))

# def asal(sayi1, sayi2):
    
#     print("1 sayisi asal degildir")
#     for sayi in range(sayi1, sayi2+1):
#         if (sayi > 1):
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
            
#             else:
#                 print(sayi)
       
# asal(sayi1, sayi2)


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
    return  tamBolenler
print(tamBolenleriBul(20))



