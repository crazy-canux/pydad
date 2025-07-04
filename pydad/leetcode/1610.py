#! /usr/bin/env python3
"""
给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。
最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。
对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。
同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。
返回你能看到的点的最大数目。

示例 1：
输入：points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
输出：3
解释：阴影区域代表你的视野。在你的视野中，所有的点都清晰可见，尽管 [2,2] 和 [3,3]在同一条直线上，你仍然可以看到 [3,3] 。o
示例 2：
输入：points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
输出：4
解释：在你的视野中，所有的点都清晰可见，包括你所在位置的那个点。
示例 3：
输入：points = [[1,0],[2,1]], angle = 13, location = [1,1]
输出：1
解释：如图所示，你只能看到两点之一。

提示：
1 <= points.length <= 105
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100

方法一：二分查找
思路

题目本身为几何问题，需要求出在视角范围内 [d−angle/2,d+angle/2] 内最多的点的覆盖数。在本题中视角可转换为相对于 location 的「极角」。首先将所有点 p 的坐标转化为相对于 location 的极角，设点 p 相对于 location 的极角为 d 
p
​
 ，找到坐标的极角处于区间 [d 
p
​
 ,d 
p
​
 +angle] 的最大数量即可。

极角转换时，已知两点的坐标可以通过反三角函数来进行转换，一般可以通过反余弦 acos，反正弦 asin，反正切 atan 等函数来确定，但以上函数的返回值范围最多只能覆盖 π，可以利用函数 atan2，不同的语言实现可以参考不同语言的标准库函数。以 C++ 为例，「atan2」的返回值范围为 [−π,π]，它的覆盖范围为 2π。

我们将所有坐标的相对于 location 极角全部求出，并按照极角的大小进行排序，我们遍历每个坐标 p 
i
​
 =(x 
i
​
 ,y 
i
​
 )，我们设 p 
i
​
  的相对于 location 的极角为 d 
p 
i
​
 
​
 ，此时需要求出所有满足坐标的极角大小处在 [d 
p 
i
​
 
​
 ,d 
p 
i
​
 
​
 +angle] 范围内的最大数目，可以利用二分查找快速的统计出处在 [d 
p 
i
​
 
​
 ,d 
p 
i
​
 
​
 +angle] 的元素数目。特别注意的是，由于存在 d 
p 
i
​
 
​
 +angle>180° 的情况，可以在原数组中将每个元素 d 
p 
i
 +360° 添加到原数组的后面，这样即可防止反转的问题。
在求极角时，对于坐标刚好处于 location 的元素需要单独进行统计，因为当 atan2 的两个参数都为 0 时，atan2 的返回值可能是未定义的，因此我们要尽量避免这种情况发生，所以需要将位于 location 的坐标进行单独统计。

复杂度分析
时间复杂度：O(nlogn)，其中 n 为坐标的个数，由于需要对所有的极角进行排序，再对每一个坐标的区间进行二分查找，因此总的时间复杂度应该为 O(nlogn+2nlog(2n))=O(nlogn)。
空间复杂度：O(n)，其中n 为坐标的个数，我们总共最多需要两倍坐标个数的空间来存储坐标的极角。

"""
from math import atan2, degrees
from bisect import bisect_right

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        sameCnt = 0
        polarDegrees = []
        for p in points:
            if p == location:
                sameCnt += 1
            else:
                polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polarDegrees.sort()

        n = len(polarDegrees)
        polarDegrees += [deg + 2 * pi for deg in polarDegrees]

        degree = angle * pi / 180
        maxCnt = max((bisect_right(polarDegrees, polarDegrees[i] + degree) - i for i in range(n)), default=0)
        return maxCnt + sameCnt

# 示例测试
if __name__ == "__main__":
    s = Solution()
    print(s.visiblePoints([[2,1],[2,2],[3,3]], 90, [1,1]))  # 输出: 3
    print(s.visiblePoints([[2,1],[2,2],[3,4],[1,1]], 90, [1,1]))  # 输出: 4
    print(s.visiblePoints([[1,0],[2,1]], 13, [1,1]))  # 输出: 1