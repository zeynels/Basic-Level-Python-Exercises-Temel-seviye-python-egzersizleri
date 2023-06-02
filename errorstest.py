# import re
# liste = ["1","2","5a","10b","abc"]
# sayiliste = []
# try: 
#      for x in liste:
#        if re.search("[^0-9]",x):
#           raise Exception(f"sadece rakamlardan oluşur: {x}")
          
#        else:
#           sayiliste.append(x)
#           print(f"Yalnizca sayisal değerler alınır {x}")
# except Exception as e:
#     print(f"Hata: {e}")
   
    
# finally:
#    print(sayiliste)
#    print("islem bitti")

#####################################################

# liste = ["1","2","5a","10b","abc"]

# for x in liste:
#     try:
#      result = int(x)
#      print(result)
#     except ValueError:
#        continue

#####################################################
# import re
# test = "q"
# while True:
#     sayi = input("Sadece sayisal değeri giriniz q girdiğinizde program sonlanır")
#     try:
#         if sayi == test:
#          break
#         elif re.search("[^0-9]",sayi):
#            continue
        
#         else:
#            continue
#     except ValueError:
#        print("Sayisal değer giriniz")


#####################################################

    
# while True:
#     sayi = input("Sayi:")

#     if sayi == "q":
#         break
#     try:
#         sayi = float(sayi)
#         print("Girdiğiniz sayı")
#     except ValueError:
#         print("Geçersiz sayı")

#####################################################
# import re

# def sifrekontrol(sifre):
#   if re.search("[çığöşü]", sifre):
#       raise TypeError("Türkçe karakter kullanmayınız")
#   else:
#       print("Geçerli parola")
# sifre = input ("Şifre belirleyiniz(Türkçe karakter kullanmayınız): ")



# try:
#    sifrekontrol(sifre)
# except TypeError as err:
#   print(err)

#####################################################


def faktoriyel(x):
    x =int(x)
    if( x< 0):
        raise ValueError("Negatif değer")
    
    result = 1
    for i in range(1,x+1):
        result *= i
    
    return result




for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    
    except ValueError as err:
        print(err)
        continue
    print(y)