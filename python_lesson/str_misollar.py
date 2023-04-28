'''
        ----------- 1 task ----------

-> Eng katta satrni uzunligi ?
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6

        ----------- 2 task ----------

-> Nuqtalar [.] ?

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

        ----------- 3 task ----------
-> jewels belgilari stones belgilari ichida nechta ?

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0
'''
# p = float('inf')
#                     1 task
# s = ["alice and bob","i think","this"]
# '''
# 2 1
# '''
# count = float('inf')
# index = 0
# for i , v in enumerate(s):
#     if count > len(v.split()):
#         count = len(v.split())
#         index = i
# print(index , count)


# ----------------------------------------

# a = [1, 23, 3, 5]

'''
1 + 23 + 3 + 5 = 32
1 + 2 + 3 + 3 + 5 = 14
32 - 14 = 18
'''
'''


-> Nuqtalar [.] ?

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''
# address = "1.1.1.1"
# print(address.replace('.', '[.]'))

'''
-> jewels belgilari stones belgilari ichida nechta ?

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0
'''
# jewels = ''.join(set("aaA"))
# stones = "aAAbbbb"

# '123'
# e = [1, 2, 3]
#
# o = list(map(str , e))
# print(''.join(o))


# for i , v in enumerate(e):
#     e[i] = int(v)


'''    * , / , + , -
input : a = "8/2"
output: 4.0
'''
# z = "80**2"
#
# print(eval(z))

'''
input : a = ['2+10' , '50-30' , '12**2' , '60//5']

'''
# a = ['2+1' , '5-3' , '1**2' , '6+5']

# print(sum(map(eval, a)))

# c = 0
# for i in a:
#     c += eval(i)
# print(c)


# y = 'fythmgh5fvbcnbe6'
# print(sum([int(i) for i in y if i.isdigit()]))
# print(sum(map(int , filter(lambda x : x.isnumeric(),y))))
# c = 0
# for i in y:
#     if i.isnumeric():
#         c += int(i)
# print(c)



a = 'e1h0l2o4l3'
r = []
for _ in range(len(a)//2):
    r.append(a[:2])
    a = a[2:]
print(r)

for i in r:
    print(i)

# r.sort(key=lambda x : int(x[0]))
# print(r)
# sorted(r , key=lambda x : int(x[0]))

'''hello'''






