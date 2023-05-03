# from
# yield
# [1,2,3,4,50]

from math import pow

def gen():
    yield 1
    yield 2
    yield 3

def result():
    yield from gen()


for i in result():
    print(i)