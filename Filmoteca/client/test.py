import requests

url = 'http://127.0.0.1:8000/api/films/'

response = requests.get(url)

# response_post = requests.post( url, data = {
#     "title": "Pearl",
#     "director": "Ti West",
#     "release_date": "2022-09-03",
#     "genre": "Terror"
#     }
# )

print(response.json())