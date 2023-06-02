def asalsayi(no1,no2):
 for sayi in range(no1,no2 + 1):
    if (sayi >1 ):
        for i in range(2,sayi):
            if sayi % i ==0:
                break
            else:
                print(sayi)
                break
asalsayi(5, 25)