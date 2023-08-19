# Need to convert list into dictionary
l = [2, 1, -10, 3, 2, 3, 1, 1, 2, 1, 3, 3, 3, 9]
d = {}
for i in range(len(l)):
    d[l[i]] = l.count(l[i])
print(d)
