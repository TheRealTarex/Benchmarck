def calculateAverage(list: list):
    SumList = sum(list)
    average = SumList / len(list)

    return average

def calculateProgress(count, max):
    progress = (count + 1) / max * 100

    return progress