'''
Given a singly linked list, determine if it is a palindrome.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half, copied from reverseList.py
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        # now head and prev are the two end nodes from left and right
        while prev:
            if prev.val != head.val:
                return (False)
            else:
                prev = prev.next
                head = head.next

        return (True)
