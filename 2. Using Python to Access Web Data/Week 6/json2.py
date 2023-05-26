import urllib.request
import json

# https://py4e-data.dr-chuck.net/comments_42.xml
# https://py4e-data.dr-chuck.net/comments_1433289.xml
url = input("Enter location: ")

print("Retrieving", url)
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

json_data = json.loads(data)
counts = json_data['comments']

# Compute the sum of the numbers
sum = 0
for comment in counts:
    sum += comment['count']

print("Count:", len(counts))
print("Sum:", sum)
