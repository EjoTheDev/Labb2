import platform
import psutil
import math


def GetPCInfo():
    Result = "\nName: "
    Result += platform.node()
    Result += "\nOS: "
    Result += platform.platform()
    Result += "\nCPU: "
    Result += platform.processor()
    Result += "\nArchitecture: "
    Result += platform.machine()
    Result += "\nMemory: "
    Result += str(math.ceil(psutil.virtual_memory().total/(1024.**3))) + "GB"
    Result += "\nMemory Usage: "
    Result += str(psutil.virtual_memory().percent) + "%"
    Result += "\nPython Version: "
    Result += platform.python_version()
    return Result
print(GetPCInfo())
