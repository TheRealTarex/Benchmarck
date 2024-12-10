from timeit import default_timer as timer
import os
import time

def doSingleBench():
    start = timer()
    for i in range(1000000):
        pass
    return timer() - start

def doBench():
    length = 1000
    benchResults = []
    last_progress = 0

    for benchCount in range(length):
        benchResults.append(doSingleBench())

        # Fortschritt berechnen und nur anzeigen, wenn er sich geändert hat
        progress = int((benchCount + 1) / length * 100)
        if progress > last_progress:
            print(f"Progress: {progress}%")
            last_progress = progress

    ResultSum = sum(benchResults)
    print("Benchmark done!")
    print(f"Result: {ResultSum}")

if __name__ == "__main__":
    doBench()