
import json


person_string = '{"name":"Ali", "languages":["python", "c#"]}'

result = json.loads(person_string)

print(result)