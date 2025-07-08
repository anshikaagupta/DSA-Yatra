# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        count=0
        for node in lists:
            if node:
                heappush(heap,(node.val, count, node))
                count+=1
        dummy=ListNode(0)
        tail=dummy
        while heap:
            val, _, node=heappop(heap)
            tail.next=node
            tail=tail.next
            if node.next:
                heappush(heap, (node.next.val, count, node.next))
                count+=1
        return dummy.next
        