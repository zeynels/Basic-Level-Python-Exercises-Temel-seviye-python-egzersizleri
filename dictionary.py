# plakalar = {"kocaeli" : 41, "istanbul": 34 }

# # print(plakalar["kocaeli"])
# # print(plakalar["istanbul"])

# # plakalar["ankara"] = 6
# # plakalar["kocaeli"] = "new value"
# # print(plakalar)

# users = {

#     "zeynelsartik": {"yas" : "20" , "mailadresi": "zeynel@gmail.com",
#     "adres": "adana", "phone": "12543"},

#     "zeynepsartik": 21

# }
# print(users["zeynelsartik"])

###############################


# ogrenciler = {
#     "120" :{
#     "ad": "ali",
#     "soyad": "yilmaz"
#     "telefon": "532 000 00 01"
# },
#     "125": {
        
#     "ad": "can",
#     "soyad": "korkmaz"
#     "telefon": "532 000 00 02"

#     },
#      "128": {
        
#     "ad": "volkan",
#     "soyad": "yükselen"
#     "telefon": "532 000 00 03"

#     } 
 


# }

ogrenciler = {}

Numara = input("Ogrenci No")
isim= input("Ogrenci Adi")
soyad= input("Ogrenci soyadi")
telefon= input("Tel no")
ogrenciler [Numara] = {

    "ad": isim,
    "surname ": soyad,
    "Tel no"  : telefon

}

# print(ogrenciler)
ogrenciler.update({
    Numara: {
        "ad" : isim,
        "surname": soyad,
        "Tel no": telefon

    }
})
Numara = input("Ogrenci No")
isim= input("Ogrenci Adi")
soyad= input("Ogrenci soyadi")
telefon= input("Tel no")
ogrenciler.update({
    Numara: {
        "ad" : isim,
        "surname": soyad,
        "Tel no": telefon

    }
})
Numara = input("Ogrenci No")
isim= input("Ogrenci Adi")
soyad= input("Ogrenci soyadi")
telefon= input("Tel no")

ogrenciler.update({
    Numara: {
        "ad" : isim,
        "surname": soyad,
        "Tel no": telefon

    }
})

print("*"*50)
ogrNo = input("öğrenci no:")
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız{Numara} nolu ogrencinin adi{ogrenci[isim]} soyadi {ogrenci[soyad]} telefon numarasi {ogrenci[telefon]}")

