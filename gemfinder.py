import requests
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Description", "Url", "Created Date", "Updated", "Language", "Stars"]

#query= "cryptocurrency+language:assembly&sort=stars&order=desc"
query= "cryptocurrency+stars:0..30"
#first page
#page=1

#search for the top repositories
#api_url = "https://api.github.com/search/repositories?q={query}&{page}"
url = 'https://api.github.com/search/repositories?q=cryptocurrency+stars:<10&sort=stars&order=asc&per_page=100'

#send get request
response = requests.get(url)

#get the json data
data =  response.json()

for repository in data["items"]:
    #name = repository["full_name"]
    description = repository["description"]
    created_date = repository["created_at"]
    recently_updated = repository["updated_at"]
    url = repository["html_url"]
    language = repository["language"]
    stars = repository["stargazers_count"]
    
    table.add_row([description, url ,created_date, recently_updated, language, stars])

print(table)