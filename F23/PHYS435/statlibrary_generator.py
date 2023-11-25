import requests
import json

url = "http://localhost:3223/api/characters"

dictionary = {
    "char": {
        "rarity": 7,
        "level": 85,
        "gear": 13,
        "equipped": "all",
    }
}

for i in range(1, 10):
    dictionary["char"]["relic"] = i

    response = requests.get(url, params={"useValues": json.dumps(dictionary)})

    if response.status_code == 200:
        with open(f'chardata_R{i}.json', 'w') as f:
            f.write(json.dumps(response.json(), indent=4))
    else:
        print(f"Request failed for relic level {i} with status code {response.status_code}")