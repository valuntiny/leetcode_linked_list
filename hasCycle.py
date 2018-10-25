'''
Given a linked list, determine if it has a cycle in it.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        try:
            fast = slow = head
            while fast.next.next and slow.next:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return (True)
            return (False)
        except:
            return (False)