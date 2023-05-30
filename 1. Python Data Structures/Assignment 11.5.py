import re

hand = open("regex_sum_1433285.txt")
x = list()
for line in hand:
    y = re.findall('\d+', line)
    x = x + y
a = 0
for i in x:
    a = a + int(i)

print(a)
