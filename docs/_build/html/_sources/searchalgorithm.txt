.. _searchalgorithm:

search algorithm
================

七大查找算法

* sequential search(顺序查找)

    顺序查找又叫线性查找.

    从第一个到最后一个和要查找的内容比较.

    时间复杂度： 最差O(log(n)), 最佳O(1), 平均O(log(n))
    空间复杂度：

* binary search(二分查找)

    二分查找又叫折半查找.只能用于有序序列。

    设置三个下标，min=0, max=array.length - 1, mid = (min+max)/2。
    然后用要查找的关键值key和mid下标的元素比较。
    如果key比array[mid]大，那么将数组一分为二，min变为mid+1,mid重新计算。
    如果key比array[mid]小，那么数组一分为二，max变为mid-1,mid重新计算。
    如果key==array[mid]那么找到了。
    如果min>=max那么没有找到。
    依次类推，每次将数组一分为二。

    时间复杂度：
    空间复杂度：

* insertion search(插值查找)

* fibonacci search(斐波拉切查找)

* tb search(树表查找)

    树表查找分为二叉树查找,2-3树查找,红黑树查找,B树和B+树查找.

* block search(分块查找)

* hash search(哈希查找)

