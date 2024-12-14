import cpuinfo
import GPUtil
import platform
import psutil
import json

def calculateAverage(list: list):
    SumList = sum(list)
    average = SumList / len(list)

    return average

def calculateProgress(count, max):
    progress = (count + 1) / max * 100

    return progress

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def getSystemInfo():
    #define libaries
    svmem = psutil.virtual_memory()
    uname = platform.uname()
    gpus = GPUtil.getGPUs()

    #get GPU and CPU infos
    gpuName = gpus[0].name
    cpuName = cpuinfo.get_cpu_info()['brand_raw']

    #get system infos
    nodeName = uname.node
    releaseName = uname.release
    systemID = uname.system
    versionName = uname.version
    systemAlias = platform.system_alias(systemID, releaseName, versionName)
    systemName = f"{systemAlias[0]} {systemAlias[1]}"

    #get memory infos
    memoryTotal = get_size(svmem.total)
    memoryAvailable = get_size(svmem.available)
    memoryUsed = get_size(svmem.used)
    memoryPercent = svmem.percent

    systemInfo = {0:gpuName, 1:cpuName, 2:nodeName, 3:systemName, 4:memoryTotal, 5:memoryAvailable, 6:memoryUsed, 7: memoryPercent}
    return systemInfo

def printSystemInfo():
    systemInfo = getSystemInfo()

    print(f"="*10, "System Info", "="*10)
    print(f"Gpu Name: {systemInfo[0]}")
    print(f"Cpu Name: {systemInfo[1]}")
    print(f"Node Name: {systemInfo[2]}")
    print(f"System Name: {systemInfo[3]}")
    print(f"="*10, "Memory Info", "="*10)
    print(f"Memory Total: {systemInfo[4]}")
    print(f"Memory Available: {systemInfo[5]}")
    print(f"Memory Used: {systemInfo[6]}")
    print(f"Memory Percent: {systemInfo[7]}")

if __name__ == "__main__":
    #printSystemInfo()
    pass