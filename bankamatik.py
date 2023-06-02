

zeynelHesap ={
    "ad" : "Zeynel Sartık" ,
     "hesapNo" : "13245678",
     "bakiye": 3000,
     "ekHesap" : 2000

}
AliHesap ={
    "ad" : "Ali Sartık" ,
     "hesapNo" : "12345678",
     "bakiye": 2000,
     "ekHesap" : 1000

}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("Paranizi alabilirsiniz")
    # elif hesap['bakiye'] <= miktar:
    #     print("Ek hesabinizi kullanmak ister misiniz")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = (input("Ek hesap kullanilsin mi? e/h"))
            
            if ekHesapKullanimi == "e":
                ekhesapkullanilacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapkullanilacakmiktar
                print("Paranizi alabilirsiniz")

            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']}")
        else:
            print("Üzgünüz paranız yetersiz")
paraCek(zeynelHesap, 3000)
paraCek(zeynelHesap, 2000)