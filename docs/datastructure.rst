.. _datastructure:

data structure
==============

数据结构

逻辑结构: 线性结构，集合结构，树形结构，图形结构。

物理结构:


String/字符串
-------------

* KMP算法
* BM模式匹配算法
* BF算法


Vector/向量
------------

顺序线性表，是一种动态数组，长度可以动态增长的顺序存储结构。

***

Stack/栈
---------

LIFO，后进先出的数据结构。只能在一端进行插入（push）和删除（pop）。

* 广义表/Generalized List
* 双端队列/Deque

***

Queue/队列
-----------

FIFO，队列是先进先出的线性数据结构。

python的collections.deque。

* 链表实现
* 循环数组实现
* 双端队列
* 优先队列
* 循环队列

***

Linked List/链表
----------------

* 单向链表/Singly linked lists
* 双向链表/Double linked lists
* 循环链表/Circular linked lists
* 静态链表/Static linked Lists
* 对称矩阵/Symmetric Matrix
* 稀疏矩阵/Sparse Matrix

***

Hash Table/哈希表
------------------

哈希表也叫散列表，基于键值对的映射关系。

python的dict就是哈希表。

* 散列函数/Hash Function
* 填充因子/Collision Resolution

***

Tree/树
--------

* 二叉树/Binary Tree

二叉树是每个节点最多有两个子节点的树形数据结构。

root：根节点

父节点，子节点，叶子节点（没有子节点）。

高度：节点到叶子节点的最长路径长度。

深度：从根到某个节点的路径长度。

子树：节点及其所有子孙组成的树。

前序遍历：root -> left -> right

中序遍历：left -> root -> right

后序遍历：left -> right -> root

层序遍历BFS：从上到下，从左到右。

* 满二叉树FBT

Full Binary Tree.

所有非叶子节点都有2个子节点，且所有叶子在同一层。

* 完全二叉树CBT

Complete Binary Tree.

除最后一层，其它层节点都填满，最后一层节点都是靠左对齐（从左开始填充）。

* 二叉搜索树BST

Binary Search Tree.

左子树所有值 < 当前节点值 <  右子树所有值

* 平衡二叉搜索树

左右子树高度差<=1

***

Heap/堆
--------

堆是特殊树形数据结构，通常是完全二叉树。

* 数组实现的堆
* 树实现的堆

***

Graph/图
---------

***

fibonacci sequence
-------------------

斐波那契数列,也叫黄金分割数列::

    0, 1, 1, 2, 3, 5, 8, 13, ...
    seq[0] = 0
    seq[1] = 1
    seq[n] = seq[n-1] + seq[n-2] (n>=2)
