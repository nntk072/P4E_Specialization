"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have
accumulated the counts for each hour, print out the counts, sorted by hour as shown below. """
name = input("Enter file: ")
handle = open(name)
counts = dict()
for i in handle:
    if not i.startswith("From "):
        continue
    else:
        i = i.split()
        i = i[5]
        hour = i[0:2]
        counts[hour] = counts.get(hour, 0) + 1
lst = list()
for key, val in counts.items():
    lst.append((key, val))
lst.sort()
for val, key in lst:
    print(val, key)
