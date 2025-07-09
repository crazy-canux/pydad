#!/usr/bin/env python3
"""
Linked list

"""
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    # print
    def __repr__(self):
        if self.next:
            return f"{self.val}->{self.next!r}"
        return f"{self.val}->None"
    
    # for
    def __iter__(self):
        curr = self
        while curr:
            yield curr.val
            curr = curr.next

def list_to_linked_list(lst: list) -> ListNode:
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for value in lst[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

def reverse(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def has_cycle(head: ListNode) -> bool:
    slow = fast = head # both move to head
    while fast and fast.next: # use fast, because fast reach the end first if not cycle list.
        slow = slow.next # slow move to next 
        fast = fast.next.next # fast move to next.next
        if fast is slow:
            return True
    return False

def merge_two_ordered_linked_list(list1, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    curr = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return dummy.next

# delete duplicated node
def delete_duplicate_from_ordered_linked_list(head: ListNode) -> ListNode:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def delete_duplicate_from_linked_list(head: ListNode) -> ListNode:
    exist = set()
    prev = None
    curr = head
    while curr:
        if curr.val in exist:
            prev.next = curr.next
        else:
            exist.add(curr.val)
            prev = curr
        curr = curr.next
    return head

def kth_to_last(head: ListNode, k: int) -> int:
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val

def delete_node(node: ListNode):
    if node is None or node.next is None:
        return
    node.val = node.next.val
    node.next = node.next.next

# palindrome, [1,2,3,2,1]
def is_palindrome(head: ListNode) -> bool:
    values = []
    curr = head
    while head:
        values.append(curr.val)
        curr = curr.next
    return values == values[::-1]

def get_intersection(head_a, head_b: ListNode) -> ListNode:
    curr_a = head_a
    while curr_a:
        print(curr_a)
        curr_b = head_b
        while curr_b:
            print(curr_b)
            if curr_a is curr_b: # use is instead of ==, because the node must have the same pre and next.
                return curr_a
            else:
                curr_b = curr_b.next
        curr_a = curr_a.next
    return None


if __name__ == "__main__":
    # head0 = ListNode(1, ListNode(2, ListNode(3, None)))
    # print(reverse(head0))

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3, head)
    # print(has_cycle(head0))
    # print(has_cycle(head))

    # head2 = ListNode(1, ListNode(2, None))
    # print(has_cycle(head2))

    # lst = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
    # head3 = list_to_linked_list(lst)
    # print(has_cycle(head3))
    # for val in head3:
    #     print(val)

    # list1 = list_to_linked_list([1, 2, 4])
    # list2 = list_to_linked_list([1, 3, 4])
    # print(merge_two_ordered_linked_list(list1, list2))

    # print(delete_duplicate_from_ordered_linked_list(list_to_linked_list([1,2,2,3,4,4,5])))

    # print(delete_duplicate_from_linked_list(list_to_linked_list([1,2,5,3,2,1])))

    # print(kth_to_last(head3, 3))
    # print(get_intersection(list_to_linked_list([4,1,8,4,5]), list_to_linked_list([5,0,1,8,4,5])))