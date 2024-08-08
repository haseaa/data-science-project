# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = list1
        head2 = list2
        mergeHead = ListNode()
        currentNode = mergeHead
        while head1 and head2:
            if head1.val <= head2.val:
                currentNode.next = head1
                head1 = head1.next
            else:
                currentNode.next = head2
                head2 = head2.next
            currentNode = currentNode.next
        while head1:
            currentNode.next = head1
            head1 = head1.next
            currentNode = currentNode.next
        while head2:
            currentNode.next = head2
            head2 = head2.next
            currentNode = currentNode.next
        mergeHead = mergeHead.next
        return mergeHead
        