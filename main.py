from timeit import default_timer as timer
from utils import calculateAverage, calculateProgress
import os
import time

def doSingleBench():
    start = timer()
    for i in range(1000000):
        pass
    return timer() - start

def doBench():
    length = 1000
    benchMultThreshold = 100000
    benchResults = []
    last_progress = 0

    for benchCount in range(length):
        benchResult = doSingleBench()
        benchResults.append(benchResult)

        progress = calculateProgress(benchCount, length)

        if progress > last_progress:
            print(f"Progress: {progress}%")
            last_progress = progress

    finalResult = calculateAverage(benchResults) * benchMultThreshold
    print("Benchmark done!")
    print(f"Result: {finalResult}")

if __name__ == "__main__":
    doBench()