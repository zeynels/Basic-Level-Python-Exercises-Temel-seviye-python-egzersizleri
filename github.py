import requests

class Github:
    def __init__(self):
        self.api_url ="https://api.github.com"
        self.token = ''

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def GetRepo(self, username):
        repo = requests.get(self.api_url+'/users/'+username+'/repos')
        return repo.json()

    def createRepo(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.token, json={
                "name": name,
                "description": "This is your first repository",
                "homepage":"https://github.com",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
            })   
        return response.json()

github = Github()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Creat Repositories\n4- Exit\n Seçiminiz:")


    if secim == "4":
        break
    else:
        if secim == "1":
            username = input('username: ')
            result = github.getUser(username)
            print(f"name {result['name']}\n public repos: {result['public_repos']}\n follower: {result['followers']}")
        elif secim =="2":
            username = input('username: ')
            result = github.GetRepo(username)
            for i in result:
                print(i['name'])

        elif secim =="3":
            name = input("Repository adını gir: ")
            result = github.createRepo(name)
            print(result)
        else:
            print("Yanlış seçim")