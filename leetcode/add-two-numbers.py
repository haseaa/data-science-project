# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        current = 0
        while head1 and head2:
            head1.val = head1.val + head2.val + current
            if head1.val > 9:
                head1.val = head1.val - 10
                current = 1
            else:
                current = 0
            if head1.next is None and head2.next is None:
                if current == 1:
                    head1.next = ListNode(1)
                return l1
            head1 = head1.next
            head2 = head2.next

        while head1:
            head1.val = head1.val + current
            if head1.val > 9:
                head1.val = head1.val - 10
                current = 1
            else:
                current = 0
            if head1.next is None:
                if current == 1:
                    head1.next = ListNode(current)
                return l1
            head1 = head1.next
        if head2:
            currentL1 = l1
            while currentL1.next:
                currentL1 = currentL1.next
            while head2:
                head2.val = head2.val + current
                if head2.val > 9:
                    head2.val = head2.val - 10
                    current = 1
                else:
                    current = 0
                currentL1.next = head2
                currentL1 = currentL1.next
                if head2.next is None:
                    if current == 1:
                        currentL1.next = ListNode(1)
                    return l1
                head2 = head2.next
            return l1
                