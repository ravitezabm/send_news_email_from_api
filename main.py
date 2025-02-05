import requests
from send_email import send_mail

url = "https://newsapi.org/v2/everything?q=india&"\
      "from=2025-01-05&sortBy=publishedAt&apiKey=55424ced9def468a9c81b29e50e27a8b"
request = requests.get(url)
username = "abhiramanrs200@gmail.com"
content = request.json()
message =""

for article in content['articles']:
      if article["title"] is not None:
            message=message + article["title"] + "\n" + article["description"] + 2* "\n"

message = message.encode('utf-8')

print(type(message))
print()
send_mail(msg=message)

