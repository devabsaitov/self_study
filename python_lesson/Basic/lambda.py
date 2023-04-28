
nums = [0,1,2,3,4]
index = [0,1,2,2,1]

r = []
for i in range(len(nums)):
    r.insert(index[i] , nums[i])
print(r)

