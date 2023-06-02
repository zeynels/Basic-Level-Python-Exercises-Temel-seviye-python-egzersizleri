import requests

class theMovieDb:
    def __init__(self):
        self.api_url ="https://api.themoviedb.org/3/"
        self.api_key = "f22059c09bfce037a2424941daeb32be"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json
movieabi = theMovieDb()
while True:
    secim = input("1-Popular Movies\n2- Search\n3- Logout\nSeçiminiz:")


    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieabi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        elif secim == "2":
            keyword = input("keyword: ")
            movies = movieabi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])

        