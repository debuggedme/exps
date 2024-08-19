class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1, list2):
    dummy = ListNode()
    node1, node2 = list1, list2
    node = dummy
    while node1 and node2:
        if node2.val <= node1.val:
            node.next = node2
            node2 = node2.next
        else:
            node.next = node1
            node1 = node1.next
        node = node.next
    while node1:
        node.next = node1
        node1 = node1.next
        node = node.next
    while node2:
        node.next = node1
        node2 = node2.next
        node = node.next
    return dummy.next