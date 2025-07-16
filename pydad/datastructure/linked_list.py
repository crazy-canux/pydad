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

# convert list to linked list.
def list_to_linked_list(lst: list) -> ListNode:
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for value in lst[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

# revert linked list
def reverse(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# 判断链表是否有环
def has_cycle(head: ListNode) -> bool:
    slow = fast = head # both move to head.
    while fast and fast.next: # use fast, because fast reach the end first if not cycle list.
        slow = slow.next # slow move to next.
        fast = fast.next.next # fast move to next.next.
        if fast is slow:
            return True
    return False

# 合并两个排序链表
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

# 删除排序链表中重复节点
def delete_duplicate_from_ordered_linked_list(head: ListNode) -> ListNode:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# 删除没有排序的链表中重复节点
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

# 返回倒数第k个节点。
def kth_to_last(head: ListNode, k: int) -> int:
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val

# 回文结构，palindrome, [1,2,3,2,1]
def is_palindrome(head: ListNode) -> bool:
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values == values[::-1]

# 链表相交, 此方法时间复杂度太大
def get_intersection_v1(head_a, head_b: ListNode) -> ListNode:
    curr_a = head_a
    while curr_a:
        curr_b = head_b
        while curr_b:
            if curr_a is curr_b: # use is instead of ==, because the node must have the same pre and next.
                return curr_a
            else:
                curr_b = curr_b.next
        curr_a = curr_a.next
    return None

# a+(b-c) == b+(a-c)
# 时间复杂度：O(M+N), 空间负责度O(1)
def get_intersection(head_a, head_b: ListNode) -> ListNode:
    a, b = head_a, head_b
    while a is not b:
        a = a.next if a else head_b
        b = b.next if b else head_a
    return a

# 移除链表节点
def delete_node_by_value(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    prev, curr = dummy, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next


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
        
    # print(is_palindrome(list_to_linked_list([1,2,3,2,1])))
    
    # print(delete_node_by_value(list_to_linked_list([1,2,3]), 3))
    
    # list_to_linked_list 不能创建相交链表，就不能用is。
    common = list_to_linked_list([8,4,5])
    a1 = ListNode(4)
    a2 = ListNode(1)
    a1.next = a2
    a2.next = common
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b1.next = b2
    b2.next = b3
    b3.next = common
    print(get_intersection(a1, b1))
    print(get_intersection_v1(a1, b1))
