import itertools
from collections import Counter
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self , head):
        self.head = head
    def deleteDuplicates(self):
        dummy = ListNode()
        tail = dummy
        while head:
            if head.next and head.val == head.next.val:
                while  head.next and head.val == head.next.val:
                    head = head.next

                tail.next = head.next
            else:
                tail = head
            head = head.next

        head = dummy.next
        return dummy.next

    def show(self):
        tmp = self.head
        while tmp:
            print(tmp.val , end=' ')
            tmp = tmp.next




if __name__ == '__main__':
    data = [0,0,1,1,1,1,2,3,3,4]
    head = ListNode()
    tmp = head
    for i in data:
        tmp.next = ListNode(i)
        tmp = tmp.next

    obj = Solution(head)
    obj.deleteDuplicates()
    obj.show()

