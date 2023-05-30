fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    abc = line.rstrip().split()
    for i in abc:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)
