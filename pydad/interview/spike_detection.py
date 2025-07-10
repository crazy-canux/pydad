#!/usr/bin/env python3

from typing import List
def spike(data: List[float], threshold: float) -> List[float]:
    spikes = []
    for i in range(1, len(data)-1):
        if abs(data[i] - data[i-1]) > threshold and abs(data[i] - data[i+1]) > threshold:
            spikes.append(i)
    return spikes

if __name__ == "__main__":
    data = [1, 2, 3, 100, 4, 5]
    threshold = 20
    print(spike(data, threshold))