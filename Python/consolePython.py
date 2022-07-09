import requests
import json
html = requests.get("http://agl-developer-test.azurewebsites.net/people.json")
List1 = json.loads(html.text)

Male = []
Female = []

for i in range(len(List1)):
    if List1[i]["pets"] != None:
        for j in range(len(List1[i]["pets"])):
            if List1[i]["pets"][j]["type"] == "Cat":
                if List1[i]["gender"] == "Male":
                    Male.append(List1[i]["pets"][j]["name"])
                elif List1[i]["gender"] == "Female":
                    Female.append(List1[i]["pets"][j]["name"])

Male.sort()
Female.sort()


print("Male")
for i in range(len(Male)):
    print(Male[i])
print("\n")
print("Female")
for i in range(len(Female)):
    print(Female[i])
    
# print(List1[5]["pets"][0]["type"])
