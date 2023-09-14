# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        l1=l=ListNode()
        
        while list1 and list2 :
            if list1.val< list2.val:
                l.next=list1
                list1=list1.next
            else:
                l.next=list2
                list2=list2.next
            l=l.next
        l.next=list1 or list2
        return l1.next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        