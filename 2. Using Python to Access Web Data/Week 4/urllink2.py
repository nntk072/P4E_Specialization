import urllib.request
import xml.etree.ElementTree as ET

# http://py4e-data.dr-chuck.net/comments_42.html
# https://py4e-data.dr-chuck.net/comments_1433287.html

url = input("Enter location: ")
print("Retrieving", url)
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
counts = tree.findall('.//count')

# Compute the sum of the numbers
sum = 0
for count in counts:
    sum += int(count.text)

# Print the count and sum
print("Count:", len(counts))
print("Sum:", sum)
