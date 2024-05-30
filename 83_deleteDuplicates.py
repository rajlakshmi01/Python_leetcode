class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def deleteDuplicates(head:[ListNode]) -> [ListNode]:
            while(head.next is None):
                if head.val==(head.next).val:
                    head.next.val=head.next.next.val
                    head=head.next.next
            return head
print(deleteDuplicates([1,1,2,3,3]))