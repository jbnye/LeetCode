# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head is None):
            return None
        current = head

        while(current.next is not None):
            if(current.val == current.next.val):
                current.next = current.next.next
            else:
                current = current.next
        return head

        # My first try using after but it wasnt nessissary
        # if(head is None):
        #     return None
        # current = head
        # after = head.next
        # while(after is not None):
        #     if(current.val == after.val):
        #         current.next, after = after.next, after.next
        #     else:
        #         current = after
        #         after = after.next
        # return head


    
        # Best solution on LC
        # if head==None:
        #     return
        # f=head
        # while f and f.next:
        #     if f.val==f.next.val:
        #         f.next=f.next.next
        #         continue
        #     f=f.next    
            
        # return head  