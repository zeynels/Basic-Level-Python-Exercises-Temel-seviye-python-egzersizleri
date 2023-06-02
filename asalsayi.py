
# sayi = int(input("Asal olup olmadigini sorgulayin: "))
# mod = 0
# sayac = 2
# kontrol = 0

# if sayi < sayac:
#     print("sayi asaldir")

# else:
#     mod = sayi & sayi
#     if mod ==0:
#         sayac+=1
#         if sayac<sayi:

sayi = int(input("Asal olup olmadigini sorgulayin: "))
asalmi = True

if sayi == 1:
    print("1 sayisi asal degildir")

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break
if asalmi:
        print("Sayi asal")
else:
        print("Sayi asal degildir")