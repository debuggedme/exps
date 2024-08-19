class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add(a, b, t):
    return (a + b + t) % 10, int((a + b + t) / 10)


def addTwoNumbers(l1=ListNode(val=5), l2=ListNode(val=5)):
    l1, l2 = ListNode(next=l1), ListNode(next=l2)
    dummy = ListNode()
    carry = 0
    n1, n2, n = l1.next, l2.next, dummy
    while n1 or n2 or carry:
        res, carry = add(n1.val if n1 else 0, n2.val if n2 else 0, carry)
        n.next = ListNode(val=res)
        n1, n2, n = n1.next if n1 else None, n2.next if n2 else None, n.next
    return dummy.next


addTwoNumbers()
print(add(5, 5, 0))
