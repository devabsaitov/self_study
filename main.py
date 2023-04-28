# s = ['hello', 'world', '123', 'a', 'bgkjfh', 'tgkfhkj']
# print(sorted(s , key=lambda x : len(x))[-1])


s = 51872653

print("".join(sorted(filter(lambda x : int(x) & 1 , str(s)))) + "".join(sorted(filter(lambda x : not int(x) & 1 , str(s)), reverse=True)) )