# def usalma(number):

#     def inner(power):
#         return number ** power
    

#     return inner



# two = usalma(2)
# print(two(3))
#-----------------------------------------------------------------------#

# def yetki_sorgula(page):
#     def inner(role):
#             if role== 'Admin':
#                   return "{0} rolünün {1} sayfasına ulaşabilir".format(role, page)
            
#             else:
#                 return "{0} rolünün {1} sayfasına ulaşamaz".format(role, page)
#     return inner

# user1= yetki_sorgula("Product Edit")
# print(user1("Admin"))


def islem(islem_adi):
    def toplam(*args):
        toplam =0
        for i in args:
            toplam +=i
        return toplam
    def carpim(*args):
        carpim =1
        for i in args:
            carpim *=i
        return carpim
    
    if islem_adi == "toplam":
        return toplam
    else:
        return carpim
    

toplama = islem("toplam")
print(toplama(1,5,3,48,35,1))

carpma = islem("carpma")
print(carpma(1,5,3,48,35,1))
