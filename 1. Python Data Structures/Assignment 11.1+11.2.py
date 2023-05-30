import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)
    '''
    Or alternative for finding from 'From: '
    if re.search('From:', line):
        print(line)
    if line.startswith('From: '):
        print(line)
    if re.search('^From:', line):  # ^From: from the beginning
        print(line)
    if re.search('^X-\S+:', line):
        print(line)
    '''
'''x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('\d+', x)  # \d= [0-9]
print(y)
y = re.findall('[AEIOU]+', x)
print(y)
x = 'From: Using the : character'
y = re.findall('^F.+', x)
print(y)
y = re.findall('^F.+?:', x)
print(y)'''

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)  # y = re.findall('^From (\S+@\S+)', x) #

print(y)
