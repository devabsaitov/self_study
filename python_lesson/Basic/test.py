# # a = {}
# # a = set()
# # print(type(a))
# #
# # for i in map(int , ['1','2']):
# #     print(i)
# # print(map(int , ['1','2']))
#
# a = {'1','2','3','4' , '4'}
# print(set(a))
# a.add(5)
# a.add(5)
# print(a)
#
# a.clear()
# print(a)
#
# a = {1,2}
# b = a.copy()
#
# print(hex(id(a)))
# print(hex(id(b)))
# a = {'1','2','3','4' , '4'}
# print(a.discard('2'))     # delete
#
# # a = {1, 2, 3,4}
# # b = {2 , 3 , 9}
# # u = b.difference(a)
# # u.update(a.difference(b))
# # print(u)
#
#
#
# # print(a.difference(b))
# # a.difference_update(b)
# # print(a)
#
# # print(a.intersection(b))
# # a.intersection_update(b)
# # print(a)
#
# # print(a.isdisjoint(b))
# # print(a)
#
# # a = {'1', '2', '3','4'}
# # b = {2, 4}
#
# # print(a.issubset(b))
#
# # print(b.issuperset(a))
# # print(a.issubset(b))
#
# # y = input()
# # b = set()
# # for i in a:
# #     if i != y:
# #         b.add(i)
# #
# # print(b)
#
# # a.remove('3')
# # print(a)
# a = {'1', '2', '3','4'}
# b = {1,2}
# print(a.union('str'))
# print(a)
#
# a.update('str')
# print(a)
#
#
#
#
#
#
#
# '''
# discard             ->  delete
# difference          ->  farqli item
# difference_update   ->
# intersection        ->  tegishli item
# intersection_update ->
# isdisjoint
# issubset
# issuperset
# pop
# remove
# union
# update
# '''
# https://leetcode.com/problems/shuffle-the-array/
# nums = [2,5,1,3,4,7]
# n = 3
# man = []
#
# for i in range(n):
#     man.append(nums[i])
#     man.append(nums[i+n])
#
# print(man)


# [2,3,5,4,1,7]     # [x1 , y1 , x2 , y2 , x3 , y3]


# https://leetcode.com/problems/number-of-good-pairs/
# nums = [1,2,3,1,1,3]
# '''output : 4'''
#
# count = 0
# for i in range(len(nums)):
#     k = 0
#     for j in nums[i+1:]:
#         if nums[i] == j:
#             k += 1
#     count += k
# print(count)

#
#
# accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
# f = 0
# for i in accounts:
#     if f < sum(i):
#         f = sum(i)
# print(f)
#
# print(max([sum(i) for i in accounts]))

'''
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
https://leetcode.com/problems/create-target-array-in-the-given-order/
https://leetcode.com/problems/decompress-run-length-encoded-list/
'''

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# candies = [4,2,1,1,2]
# extraCandies = 1
#
# print([True if i + extraCandies >= max(candies) else False for i in candies])







# print(list(map(lambda x : x + extraCandies >= max(candies)  , candies)))

# max_ = max(candies)
# r = []
# for i in candies:
#     if i + extraCandies > max_:
#         r.append(True)
#     else:
#         r.append(False)
# print(r)


'''
# 1 usul
        r = []
        for i in candies:
            if (i+extraCandies) >= max_:
                r.append(True)
            else:
                r.append(False)
        return r

        # 2 usul
        maxx:int = max(candies) 
        return list(True if maxx<=x+extraCandies else False   for x in candies )

        # 3 usul
        return list(map(lambda x : (x+extraCandies) >= max(candies) , candies))
'''
# a = [i if i < 3 else False for i in range(0,10)]
# print(a)
#
# name = ['habibuloh' , 'sulton' , 'samir' , 'john']
# #
# print([i for i in name if i.startswith('s')])
#
# r = []
# for i in name:
#     if i.startswith('s'):
#         r.append(i)
# print(r)


# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
# r = []
# [r.insert(index[i], nums[i]) for i in range(len(nums))]
# print(r)

# https://leetcode.com/problems/decompress-run-length-encoded-list/

# r = []
# for i in range(0 , len(nums), 2): # 0 2
#     r += [nums[i+1]]*nums[i]
# print(r)
# r = []
# [r.extend([nums[i + 1]] * nums[i]) for i in range(0, len(nums), 2)]
# print(r)







'''[1,3,3,6,6,6]'''

from function import test_kwargs
test_kwargs(1,2,3 , name = 'Botirjon' , age = 20)












