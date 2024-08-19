class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head=ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3)))))):
    dummy = ListNode(next=head)
    node = dummy
    while node:
        prev = node.next
        post = prev.next if prev else None
        if (not prev or not post) or (prev and post and not prev.val == post.val):
            node = node.next
            continue
        while prev and post and prev.val == post.val:
            prev, post = prev.next, post.next
        node.next = post
    return dummy.next


deleteDuplicates()
