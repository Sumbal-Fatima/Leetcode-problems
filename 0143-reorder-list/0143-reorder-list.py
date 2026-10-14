# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return None # function ends here because either 1 or 2 nodes

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow now points to the tail of second list

        curr = slow.next
        slow.next = None

        # loop to reverse the second list
        while curr:
            temp = curr.next
            curr.next = slow
            slow = curr
            curr = temp

        # slow now points to the start of the reversed second list

        # loop to merge the two lists
        while head.next:
            temp = head.next
            head.next = slow
            slow = temp
            head = head.next