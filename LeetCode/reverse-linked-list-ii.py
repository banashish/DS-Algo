# Link for question https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None or head.next is None or left == right:
            return head
        head = ListNode('a', head)
        temp = head
        first, last = None, None

        for i in range(0, right):
            if i == left - 1:
                first = head
            head = head.next

        last = head.next

        start, end = self.reverse(first.next, last)

        first.next = start
        end.next = last

        return temp.next

    def reverse(self, first, last):
        temp = first
        prev = None
        next = first
        curr = first

        while curr is not last:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return (prev, temp)
