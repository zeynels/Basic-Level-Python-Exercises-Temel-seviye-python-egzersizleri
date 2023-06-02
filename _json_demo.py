import json
import os
class User:
    def __init__(self, username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loaduser()

    def loaduser(self):
        if os.path.exists("user.json"):
            with open("user.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username= user["user"],password= user["password"],email= user["email"])
                    self.users.append(newUser)
            
            print(self.users)


    def register(self, user: User):
        self.users.append(user)
        self.loaduser()
        self.savetofile()
        print("Kullanıcı oluşturuldu")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login yapıldı")
                break
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı")
    def idenity(self):
         if self.isLoggedIn:
           print(f"username: {self.currentUser.username}")
         else:
             print("Giriş yapılmadı")
    def savetofile(self):

        liste = []

        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        with open("user.json","w",encoding="utf-8") as file:
            json.dump(liste, file)

repository = UserRepository()
while True:
    print("Menü".center(50,"*"))
    secim = input("i- Register\n2- Login\n3- Logout\n4- idenity\n5-Exit\nSeçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')
            user = User(username=username,password=password,email=email)
            repository.register(user)
            print(repository.users)


            pass
        elif secim == "2":
            if repository.isLoggedIn:
                print("Zaten login oldunuz")
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)            
        elif secim =="3":
            repository.logout()
        elif secim =="4":
            repository.identity()
        else:
            print("Yanlış seçim")
