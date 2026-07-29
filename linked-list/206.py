"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# LeetCode 206th problem - https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]):
        # current = head
        # ll_list = []
        # while current:
        #     ll_list.append(current.val)
        #     current = current.next
        # print(ll_list)

        prev = None
        current = head

        while current:
            next_node = current.next
            print(
                f"Current: {current.val}, Next: {next_node.val if next_node else None}, Prev: {prev.val if prev else None}"
            )
            current.next = prev
            prev = current
            current = next_node
            print(
                f"After Reversal - Current: {current.val if current else None}, Next: {next_node.val if next_node else None}, Prev: {prev.val if prev else None}"
            )

        return prev


sol = Solution()
print(sol.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
