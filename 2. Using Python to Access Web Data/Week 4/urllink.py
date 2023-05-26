import urllib.request
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/known_by_Fikret.html

def get_next_link(url, position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[position - 1].get('href')

def follow_links(start_url, count, position):
    url = start_url
    for i in range(count):
        print("Retrieving:", url)
        url = get_next_link(url, position)
    return url.split('_')[-1].split('.')[0]

# Prompt the user for inputs
start_url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Follow links and retrieve the last name
last_name = follow_links(start_url, count, position)
print("The answer to the assignment for this execution is", last_name)
