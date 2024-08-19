class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head, n):
    dummy = ListNode(next=head)
    fast,slow = dummy, dummy
    i = -1
    while (i := i + 1) < n:
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next if slow.next else None