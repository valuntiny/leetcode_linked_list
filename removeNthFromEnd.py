'''
Given a linked list, remove the n-th node from the end of list and return its head.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return (head)
