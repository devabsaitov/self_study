from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            if target - v in nums and (a := nums.index(target - v)) != i:
                return [i, a]
        else:
            return [0, 0]







if __name__ == '__main__':
    b = [3,2,0,4]
    a = Solution()
    print(a.twoSum(b, 6))