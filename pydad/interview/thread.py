from threading import Thread, Lock, BoundedSemaphore
from queue import Queue
import time, math, random

task_queue = Queue()
GPU_NUM=2
TASK_NUM = 10


class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        
def producer(number):
    for i in range(number):
        task = Task(i)
        task_queue.put(task)
        print(f"task {i} submitted")
        time.sleep(random.uniform(0.1, 0.5))
    # send stop signal to all consumers
    for _ in range(GPU_NUM):
        task_queue.put(None)
    
def consumer(gpu_id):
    while True:
        task = task_queue.get()
        if task is None:
            # None 也要标记done，否则线程不会退出
            task_queue.task_done()
            break
        print(f"execute {task.task_id} on gpu {gpu_id}")
        time.sleep(random.uniform(0.5, 1.0))
        print(f"finished {task.task_id} on gpu {gpu_id}")
        task_queue.task_done()

if __name__ == "__main__":
    # consumer runs first.
    for i in range(GPU_NUM):
        Thread(target=consumer, args=(i,)).start()
    producer(TASK_NUM)
    task_queue.join() # 等待所有任务处理完毕
    print("All done")
