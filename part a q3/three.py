def probability():
    sides = 6
    total = sides ** 2
    d = {}
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            sums = i + j
            d[sums] = d.get(sums, 0) + 1
    
    for value, count in d.items():
        ans = count / total
        frac= str(count)+"/"+str(total)
        print(f"P(Sum = {value}) = {frac,ans}")

probability()