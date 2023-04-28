from collections import Counter

data = [0,0,1,1,1,1,2,3,3,4]

a = Counter(data)
print([i for i, c in a.items() if c == 1])


