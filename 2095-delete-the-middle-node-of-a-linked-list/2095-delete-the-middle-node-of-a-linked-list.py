# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 2
        tmp = head.next
        if tmp is None:
            return 
        while tmp.next is not None:
            tmp = tmp.next
            cnt += 1
        middle_pos = cnt // 2
        # print(middle_pos, cnt)
        # print(head)
        a = ListNode(val=head.val, next=None)
        lst = []
        head = head.next
        middle_pos -= 1
        while True:
            if head is None:
                break
            if middle_pos == 0:
                middle_pos -= 1
                head = head.next
                continue
            lst.append(ListNode(head.val, next=None))
            head = head.next
            if head is None:
                break
            middle_pos -= 1
        
        for i in range(len(lst)-2,-1,-1):
            lst[i].next = lst[i+1]
        if len(lst) == 0:
            a.next = None
        else:
            a.next = lst[0]
        return a
            
        