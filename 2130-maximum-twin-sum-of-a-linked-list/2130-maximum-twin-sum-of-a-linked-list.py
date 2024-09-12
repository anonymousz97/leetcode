# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        # combine the reverse the first half linked list + slow/fast to find the middle item in the linked list.
        while True:
            fast = fast.next.next
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            if fast is None:
                break
        first_item_of_1st_array = prev
        first_item_of_2nd_array = slow
        max_sum = 0
        while True:
            if first_item_of_1st_array.val + first_item_of_2nd_array.val > max_sum:
                max_sum = first_item_of_1st_array.val + first_item_of_2nd_array.val
            first_item_of_1st_array = first_item_of_1st_array.next
            first_item_of_2nd_array = first_item_of_2nd_array.next
            if first_item_of_2nd_array is None:
                break
        return max_sum
        
        
            
            
        