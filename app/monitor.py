from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
import platform

def cpu():
    return cpu_percent(interval=1)

def ram():
    return virtual_memory().percent

def disk():
    return disk_usage(r"C:" if platform.system == "Windows" else "/").percent

def system_boot_time():
    return boot_time()

if __name__ == "__main__":
    print(f"CPU: {cpu()}%")
    print(f"RAM: {ram()}%")
    print(f"Disk Usage: {disk()}%")
    print(f"System boot time: {system_boot_time()}")
