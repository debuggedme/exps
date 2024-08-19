class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy
    while (slow := slow.next) and (fast := fast.next.next if fast.next else None) and not slow == fast:
        continue
    return slow == fast
