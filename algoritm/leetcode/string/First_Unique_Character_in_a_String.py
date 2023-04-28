from collections import Counter


class Solution:
    def firstUniqChar(self, s: str):
        d = Counter(s)
        for i , v in enumerate(s):
            if d.get(v , 0) == 1:
                return i
        else:
            return -1

if __name__ == '__main__':
    s = "aabb"
    a = Solution()
    print(a.firstUniqChar(s))
