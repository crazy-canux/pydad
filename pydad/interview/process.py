from multiprocessing import Process, Queue
import time, math, random

NUM_CPU = 3
NUM_TASK = 10


class Task:
    def __init__(self, task_id):
        self.task_id = task_id

def producer(task_queue, number):
    for i in range(number):
        task_queue.put(Task(i))
        print(f"submit task {i}")
        time.sleep(random.uniform(0.1, 0.5))
    # send stop signal to all consumers.
    for _ in range(NUM_CPU):
        task_queue.put(None)

def consumer(task_queue, number):
    while True:
        task = task_queue.get()
        if task is None:
            break
        print(f"handle task {task.task_id} on {number}")
        time.sleep(random.uniform(0.5, 1.0))
        print(f"task {task.task_id} finished on {number}")

if __name__ == "__main__":
    # processing queue不能是全局变量，进程间不共享的。
    queue = Queue()

    consumer_process = [
        Process(target=consumer, args=(queue, i))
        for i in range(NUM_CPU)
    ]
    for p in consumer_process:
        p.start()

    # producer(queue, NUM_TASK)
    producer_process = Process(target=producer, args=(queue, NUM_TASK))
    producer_process.start()
    
    producer_process.join()
    for p in consumer_process:
        p.join()
        
    print("All done")
