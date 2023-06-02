import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")

result= json.loads(result.text)

for i in result:
    print(i["title"])


# print(result[0]["title"])
