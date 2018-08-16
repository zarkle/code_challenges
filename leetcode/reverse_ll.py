# https://leetcode.com/problems/reverse-linked-list/description/
# https://leetcode.com/articles/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        head = previous
        return head