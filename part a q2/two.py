result = []
for i in range(1, 7):
    l = []
    for j in range(1, 7):
        l.append(i + j)
    result.append(l)
for row in result:
    print(row)