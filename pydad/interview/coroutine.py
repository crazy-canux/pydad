#!/usr/bin/env python3

import asyncio
import random

NUM_TASK = 10
NUM_GPU = 3

class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        
async def producer(q, number):
    for i in range(number):
        await q.put(Task(i))
        print(f"task {i} submitted")
        await asyncio.sleep(random.uniform(0.1, 0.5))
    # send stop signal to consumers
    for i in range(NUM_GPU):
        await q.put(None)

async def consumer(q, number):
    while True:
        task = await q.get()
        if task is None:
            q.task_done()
            break
        print(f"processing {task.task_id} on {number}")
        await asyncio.sleep(random.uniform(0.5, 1.0))
        print(f"task {task.task_id} finished on {number}")
        q.task_done()

async def main():
    queue = asyncio.Queue()
    consumer_tasks = [
        asyncio.create_task(consumer(queue, i))
        for i in range(NUM_GPU)
    ]
    await producer(queue, 10)
    await queue.join()
    await asyncio.gather(*consumer_tasks)
    print("All done")

if __name__ == "__main__":
    asyncio.run(main())
