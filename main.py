import requests

url = "https://newsapi.org/v2/everything?q=india&"\
      "from=2025-01-05&sortBy=publishedAt&apiKey=55424ced9def468a9c81b29e50e27a8b"
request = requests.get(url)

content = request.json()

for article in content['articles']:
      print(article["title"])
      print(article["description"])
