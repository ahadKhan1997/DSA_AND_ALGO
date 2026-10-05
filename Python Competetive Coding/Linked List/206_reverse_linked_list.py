"""
https://leetcode.com/problems/reverse-linked-list/description/

206. Reverse Linked List
Solved
Easy
Topics
premium lock icon
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    # 2. Helper function to transform a Python list into a Linked List
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# 3. Helper function to print it cleanly in your console
def print_linked_list(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements) if elements else "Empty List")


py_list = [1, 2, 3, 4, 5]
head = create_linked_list(py_list)
sol = Solution()
reversed_head = sol.reverseList(head)

# Instead of standard printing, call your visual helper!
print_linked_list(reversed_head)