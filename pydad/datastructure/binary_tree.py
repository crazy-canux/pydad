#!/usr/bin/env python3

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 前序(root-left-right)，从上往下
# stack: LIFO
def pre_order_v1(node: TreeNode):
    stack = [node]
    while stack:
        curr = stack.pop()
        print(curr.value)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

def pre_order_v2(node: TreeNode):
    if node:
        print(node.value)
        pre_order_v2(node.left)
        pre_order_v2(node.right)

def pre_order(node: TreeNode) -> List[int]:
    if not node:
        return []
    else:
        return [node.value] + pre_order(node.left) + pre_order(node.right)
    
# 中序(left-root-right)
# use stack, LIFO
def in_order_v1(node: TreeNode):
    stack = []
    curr = node
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.value)
        curr = curr.right

def in_order_v2(node: TreeNode):
    if node:
        in_order_v2(node.left)
        print(node.value)
        in_order_v2(node.right)
        
def in_order(node: TreeNode) -> List[int]:
    if node:
        return in_order(node.left) + [node.value] + in_order(node.right)
    else:
        return []

# 后序 （left-right-root），从下往上
def post_order_v1(node: TreeNode):
    stack1 = [node]
    stack2 = []
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        print(stack2.pop().value)

def post_order_v2(node: TreeNode):
    if node:
        post_order_v2(node.left)
        post_order_v2(node.right)
        print(node.value)
        
def post_order(node: TreeNode) -> List[int]:
    if node:
        return post_order(node.left) + post_order(node.right) + [node.value]
    else:
        return []

# 层序遍历(BFS)，从上往下，从左往右
# Queue: FIFO
def level_order_v1(node: TreeNode):        
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        print(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
            
def level_order(node: TreeNode) -> List[int]:
    if not node:  # deque([]) is not None
        return []
    queue = deque([node])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result

# 之字形遍历

# morris遍历

#######################################
# 二叉树最大深度
def max_depth(node: TreeNode) -> int:
    if not node:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1

# 二叉树最小深度，如果一边没有就不能算。
def min_depth(node: TreeNode) -> int:
    if not node:
        return 0
    if not node.left:
        return min_depth(node.right) + 1
    if not node.right:
        return min_depth(node.left) + 1
    return min(min_depth(node.left), min_depth(node.right)) + 1

# 路径总和问题，根节点到叶子节点路径上节点总和=给定值
def has_path_sum(node: TreeNode, target: int) -> bool:
    if not node:
        return False
    if not node.left and not node.right:
        return node.value == target
    return (
        has_path_sum(node.left, target-node.value) or 
        has_path_sum(node.right, target-node.value)
    )

# 根据中序+前序/后序 构造二叉树

# 二叉树最大路径和

#######################################
# 两棵树是否相同
def is_same_tree(node1, node2: TreeNode) -> bool:
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.value != node2.value:
        return False
    return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)

# 对称二叉树
def is_symmetric(node: TreeNode) -> bool:
    if not node:
        return True
    def mirror(left, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.value != right.value:
            return False
        return mirror(left.left, right.right) & mirror(left.right, right.left)
    return mirror(node.left, node.right)

# 满二叉树判断
def is_full_tree(node: TreeNode) -> bool:
    if not node:
        return True
    if not node.left and not node.right:
        return True
    if not node.left or not node.right:
        return False
    return is_full_tree(node.left) and is_full_tree(node.right)

# 完全二叉树判断：难
def is_complete_tree(node: TreeNode) -> bool:
    pass

# 平衡二叉树判断：难
def is_balanced_tree(node: TreeNode) -> bool:
    pass

#######################################
# 二叉树搜索合法性
# Binary Search Tree
def is_valid_bst(node: TreeNode) -> bool:
    pass

# 在二叉搜索树BST中插入/删除节点

# 在BST中查找第K大/小元素

# 在BST中查找最近公共祖先

# 将有序数组转化为平衡BST

#######################################
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    
    root1 = TreeNode(1)
    root1.left = TreeNode(3, None, TreeNode(6))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(5))
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root2.right = TreeNode(2, TreeNode(4), TreeNode(3))
    
    # 1,2,4,5,3,6
    # pre_order_v1(root)
    # pre_order_v2(root)
    # print(pre_order(root))
    
    # 4,2,5,1,3,6
    # in_order_v1(root)
    # in_order_v2(root)
    # print(in_order(root))
    
    # 4,5,2,6,3,1
    # post_order_v1(root)
    # post_order_v2(root)
    # print(post_order(root))
    
    #1, 2, 3, 4,5,6
    # level_order_v1(None)
    # print(level_order(root))
    
    # print(max_depth(root))
    print(min_depth(root))
    
    # print(is_same_tree(root, root))
    # print(is_same_tree(root, root1))
    # print(is_symmetric(root2))
    # print(is_full_tree(root2))