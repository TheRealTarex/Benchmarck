from timeit import default_timer as timer
from utils import calculateAverage, getSystemInfo, printSystemInfo
import os
import time
from tqdm import tqdm

def doSingleBench():
    start = timer()
    for i in range(1000000):
        pass
    return timer() - start

def doBenchMarck():
    length = 1000
    benchMultThreshold = 100000
    benchResults = []

    for benchCount in tqdm(range(length)):
        benchResult = doSingleBench()
        benchResults.append(benchResult)

    finalResult = calculateAverage(benchResults) * benchMultThreshold
    return finalResult

if __name__ == "__main__":
    os.system("cls")
    printSystemInfo()
    time.sleep(5)
    os.system("cls")

    result = doBenchMarck()
    print("Benchmark done!")
    print(f"Result: {int(result)}")