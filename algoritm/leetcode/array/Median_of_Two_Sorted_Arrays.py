from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        change = sorted(nums1+nums2)
        if (l:=len(change)) % 2 == 1:
            return f"{change[l // 2]:.5f}"
        else:
            return f"{(change[l // 2] + change[l // 2 - 1])/2:.5f}"




if __name__ == '__main__':
    nums1 = [1, 3,4]
    nums2 = [2]
    a = Solution()
    print(a.findMedianSortedArrays(nums1, nums2))