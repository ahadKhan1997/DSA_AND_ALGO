"""
19. Remove Nth Node From End of List
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # 2. Advance fast pointer so there is a gap of n nodes between slow and fast
        for _ in range(n):
            fast = fast.next
            
        # 3. Move both pointers together until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # 4. slow is now right before the target node. Skip it!
        slow.next = slow.next.next
        
        # Return the actual head (stored safely next to dummy)
        return dummy.next