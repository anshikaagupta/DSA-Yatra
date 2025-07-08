# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        dummy=ListNode(0)
        start=dummy
        while l1 and l2:
            if l1.val<l2.val:
                start.next=l1
                l1=l1.next
            else:
                start.next=l2
                l2=l2.next
            start=start.next
        if l1:
            start.next=l1
        if l2:
            start.next=l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        mid=len(lists)//2
        left=self.mergeKLists(lists[:mid])
        right=self.mergeKLists(lists[mid:])
        return self.merge(left,right)
        