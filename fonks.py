# def sayHello(name = "user"):
#    return "Hello "+name


# msg = sayHello("Çınar")

# print(msg)

# def total(num1, num2):
#    return num1 + num2

# result = total(10,20)
# print(result)


# def yasHesapla(dogumYili):
#   return 2019 - dogumYili

# ageCinar = yasHesapla(2017)
# ageAda = yasHesapla(2010)
# ageZeynel = yasHesapla(2000)
# print(ageCinar,ageAda,ageZeynel)


# def Emeklilik(dogumYili, isim):
#    '''
#    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı hesaplayabilirsiniz
#    INPUT: Doğum Yılı
#    OUTPUT: Hesaplanan yıl bilgisi

#    '''
#    yas = yasHesapla(dogumYili)
#    emekli = 65 - yas

#    if emekli > 0:
#       print(f"Emekliliginize {emekli} yil kaldi")
#    else:
#       print("Zaten emekli oldunuz")

# Emeklilik(1980, "Ali")

# print(help(Emeklilik))


# def buyuk_harf(metin):
#     metin = metin.upper()
#     print(metin)

# buyuk_harf("torba var mı beyler")

# def selamla(mesaj, isim):
#     print(f"{mesaj} {isim}")


# selamla("naber lan ","zeynel")

# def indirim(fiyat,yuzde):
#     indirim_miktari = fiyat * (yuzde /100)
#     indirim_miktari = fiyat - indirim_miktari
#     print(f"İndirimli tutar:  {indirim_miktari}")


# indirim(1000,10)


# def topla(x,y):
#     print(x+y)
#     return x+y

# sonuc = topla(3,8)
# print(sonuc)


# def ortalama(x,y):
#     return (x+y) /2

# print(type(ortalama(3,7)))


def f(x):
    return x+10

print(f(8))


def merhaba(parametre):
    print("merhaba"+parametre)


merhaba("sadi")
merhaba("evren")