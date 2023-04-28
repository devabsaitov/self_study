


d = dict()
with open("photos.txt" , 'r') as f:
    data = "".join(f.read().split())
    for i in data:
        if not i in d.keys():
            d[i] = 0
        else:
            d[i] += 1

print(sorted(d.items(), key=lambda x: x[1])[-1])




