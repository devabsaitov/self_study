
'''
set
dict
list comprehension
zip
function
lambda
'''
#
# d = {
#     1 : 'bir',
#     2 : 'ikki',
#     3 : 'uch'
# }
# print(d[1])
#
# d[3] = 'value123e4ry657u8'
# print(d)
#
# d.get()
d = {1 : 'bir',2 : 'ikki',3 : 'uch'}

print(d.get(4))
print(d.setdefault(5))
# print(d.pop(3))
# print(d.popitem())
print(d.keys())
print(d.values())
print(d.items())
p = {0 : 9}
d.update(p)
print(d.fromkeys('123'))
print(d)


i = {
    1 : {4: {9:90}},
    5 : 20
}
print(i.get(1).get(4).get(9))




'''


fromkeys
clear
copy
'''




