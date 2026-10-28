from psutil import cpu_percent, virtual_memory, disk_usage, boot_time

def cpu():
    return cpu_percent()

def ram():
    return virtual_memory().percent

def disk():
    return disk_usage().percent

def system_boot_time():
    return boot_time()