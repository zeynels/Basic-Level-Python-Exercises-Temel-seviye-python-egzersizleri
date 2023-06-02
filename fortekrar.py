# sayi = int(input("Bir sayi giriniz: "))

# fakt= 1
# for i in range(1,sayi+1):
#     fakt*=i

# print(fakt)
# i = 1
# while i < sayi+1:
#     fakt*=i
#     i+=1
# print(fakt)
# bayrak = 0

# for i in range(1,sayi+1):
#     if sayi % i == 0:
#         bayrak+=1
    
# print(bayrak)
# if bayrak == 1:
#     print("Sayi asaldir")

# else:
#     print("Sayi asal degildir")

# sayi = str(sayi)

# toplam = 0

# for rakam in sayi:
#     toplam += int(rakam)

# print(toplam)
# liste = []
# for i in range(1,6):
#     sayi = int(input("Bir sayi giriniz"))
#     liste.append(sayi)

# print(max(liste))

sayi = int(input("Bir sayi giriniz: "))
test = 0
for i in range(1,sayi+1):
    if test == i**2:
        break

print(f"{i} sayisinin karesidir")
