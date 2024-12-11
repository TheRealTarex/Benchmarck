import cpuinfo
import GPUtil
import platform

def calculateAverage(list: list):
    SumList = sum(list)
    average = SumList / len(list)

    return average

def calculateProgress(count, max):
    progress = (count + 1) / max * 100

    return progress

def getSystemInfo():
    uname = platform.uname()
    gpus = GPUtil.getGPUs()

    gpuName = gpus[0].name
    cpuName = cpuinfo.get_cpu_info()['brand_raw']


    nodeName = uname.node
    releaseName = uname.release
    systemID = uname.system
    versionName = uname.version
    systemAlias = platform.system_alias(systemID, releaseName, versionName)
    systemName = f"{systemAlias[0]} {systemAlias[1]}"

    systemInfo = {gpuName, cpuName, nodeName, systemName}
    return systemInfo