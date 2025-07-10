#!/usr/bin/env python3

import asyncio
import random

async def ping(host: str) -> str:
    await asyncio.sleep(random.uniform(0.1, 0.5))
    if random.random() < 0.8:
        return f"{host} pong"
    else:
        return f"{host} timeout"
    
async def batch_ping(hosts: list) -> list:
    tasks = [ping(h) for h in hosts]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    hosts = ["host1", "host2", "host3", "host4", "host5"]
    results = asyncio.run(batch_ping(hosts))
    for res in results:
        print(res)    