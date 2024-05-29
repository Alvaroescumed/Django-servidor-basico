import requests

url = 'http://127.0.0.1:8000/api/catalog/'

# response_post = requests.post( url, data = {
#     "name": "Mia Goth",
#     "birth_date": "1993-10-25"
# })
# response_post = requests.post(url, data = {
#     "title": "Pearl",
#     "director": "Ti West",
#     "release_date": "2022-09-03",
#     "genre": "Horror"
# })
# print(response.json())

response = requests.get(url)


print(response)