#!/usr/bin/env python3

import heapq
from typing import List

def schedule(servers, tasks: List[int]) -> List[int]:
    heap = [(usage, index) for index, usage in enumerate(servers)]
    heapq.heapify(heap)
    sche = []
    for task in tasks:
        usage, index = heapq.heappop(heap)
        sche.append(index)
        heapq.heappush(heap, (usage+task, index))
    return sche
    

if __name__ == "__main__":
    servers = [10, 5, 2]  # 当前三台服务器已使用的资源
    tasks = [3, 6, 2]     # 三个任务要分配，分别占 3, 6, 2 单位资源
    print(schedule(servers, tasks))
