# About

This is a package of algorithm written in python.

研究python相关的高级知识,包括数据结构和算法,软件工程等.

***

# sort algorithm

* selection sort(选择排序)

    用第0个依次和后面的比较，如果第0个大就交换位置，一轮下来最小的数就在第0位置。
    用第1个依次和后面的比较，如果第1个大就交换位置，第二轮下来第二小的就在第1位置。
    ...
    依次类推,直到倒数第二个和最后一个比较。

* heap sort(堆排序)

* insertion sort(插入排序)

* shell sort(希尔排序)

* bubble sort(冒泡排序)

    用第0个和第1个比较，如果第0个大就交换位置...用倒数第二个和最后一个比较，如果第1个大就交换位置。
    第一轮就是从前往后相邻的比较，最大的数就在最后一个位置。
    用第0个和第一个比较，如果第0个大就交换位置...用倒数第三个和倒数第二个比较，如果倒数第三个大就交换位置。
    第二轮就是从前到倒数第二个相邻的比较，第二大的就在倒数第二位置。
    ...
    依次类推，最后第0个和第1个比较。

* quick sort(快速排序)

* merge sort(归并排序)

* bucket/radix sort(桶式排序/基数排序)

***

# search algorithm

* order search(顺序查找/线性查找)

    从前往后比较。

* binary search(二分查找/折半查找)

    只能用于有序数组。
    设置三个下标，min=0, max=array.length - 1, mid = (min+max)/2。
    然后用要查找的关键值key和mid下标的元素比较。
    如果key比array[mid]大，那么将数组一分为二，min变为mid+1,mid重新计算。
    如果key比array[mid]小，那么数组一分为二，max变为mid-1,mid重新计算。
    如果key==array[mid]那么找到了。
    如果min>=max那么没有找到。
    依次类推，每次将数组一分为二。

* block search(分块查找)

* hash search(哈希查找)

***

# TODO

Finish all rest and update this file.
