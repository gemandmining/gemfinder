import requests
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Url", "Created Date", "Updated", "Language", "Stars"]

#query= "cryptocurrency+language:assembly&sort=stars&order=desc"
query= "cryptocurrency+stars:0..30"
#first page
#page=1

#search for the top repositories
#api_url = "https://api.github.com/search/repositories?q={query}&{page}"
#Filtrado por stars < 5
#api_url = url = 'https://api.github.com/search/repositories?q=language:C%2B%2B+topic:cryptocurrency+stars:<5&sort=updated&per_page=10'
url = 'https://api.github.com/search/repositories?q=language:C%2B%2B+cryptocurrency+stars:<5&sort=updated&per_page=20'

#send get request
response = requests.get(url)

#get the json data
data =  response.json()

for repository in data["items"]:
    #name = repository["full_name"]
    #description = repository["description"]
    created_date = repository["created_at"]
    recently_updated = repository["updated_at"]
    url = repository["html_url"]
    language = repository["language"]
    stars = repository["stargazers_count"]
    
    table.add_row([url ,created_date, recently_updated, language, stars])

print(table)
