
# a = int(input("Bir sayi giriniz: "))
# b = int(input("Bir sayi giriniz: "))

# sonuc = a > b 

# print(f"a: {a} b: {b} den buyuktur : {sonuc} ")


# vize1 = int(input("Vize notu giriniz"))
# vize1 =0.6* vize1
# vize2 = int(input("Vize notu giriniz"))
# vize2 =0.6* vize2
# final = int(input("Final notu giriniz"))
# final =0.4* final
# sonuc = vize1*vize2*final
# gectikaldi = (sonuc >= 50)


# a = int(input("Bir sayi giriniz: "))
# sonuc =  (a%2 == 0)
# print(f"Sayi cifttir{sonuc}")
# a = int(input("Bir sayi giriniz: "))
# sonuc =  (a>0)
# print(f"Sayi pozitiftir {sonuc}")

email = "a@gmail.com"
password = "1234"

girilenemail = input("email: ")
girilenesifre = input("Sifre: ")

isEmail = (email == girilenemail)
isSifre = (password == girilenesifre)

print(f"E mail dogru: {isSifre} Sifre dogru: {isEmail}")

