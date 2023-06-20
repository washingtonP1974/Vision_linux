#!/usr/bin/python3
# coding: utf-8

import datetime
import subprocess
import platform
import multiprocessing

import sys
import subprocess
from scapy.all import srp, Ether, ARP
from speedtest import Speedtest

print("__________________________ :           bY m0rg4n/b1n/b45h  2023            : __________________________________")
print("\n")
now = datetime.datetime.now()
day_of_week = now.strftime('%A')
day = now.day
month = now.strftime('%B')
year = now.year
hours = now.hour
minutes = now.minute
seconds = now.second
print("Day of the week:", day_of_week, end=", ")
print("Day:", day, end=" ")
print("Month:", month, end=" ")
print("Year:", year, end=", ")
print("Time:", f"{hours:02d}:{minutes:02d}:{seconds:02d}")
print("\n")

print(":::::::::::::::::::::::::  :         Your hardware information is:")

def check_disk_space():
    # Check disk space usage
    print("Disk Space Usage:")
    df_output = subprocess.check_output(["df", "-h"]).decode("utf-8")
    print(df_output)

def check_memory_usage():
    # Check memory usage
    print("Memory Usage:")
    free_output = subprocess.check_output(["free", "-m"]).decode("utf-8")
    print(free_output)

def check_process_status():
    # Check process status
    print("Process Status:")
    ps_output = subprocess.check_output(["ps", "aux"]).decode("utf-8")
    print(ps_output)

# Call the functions to check for errors
check_disk_space()
check_memory_usage()
check_process_status()
print("\n")

def get_processor_info():
    # Get processor information
    processor = platform.processor()
    print(f"Processor: {processor}")

def get_processing_units_info():
    # Get information about processing units (CPU cores)
    num_physical_cores = multiprocessing.cpu_count()
    num_logical_cores = multiprocessing.cpu_count()
    print(f"Number of Physical Cores: {num_physical_cores}")
    print(f"Number of Logical Cores: {num_logical_cores}")
print("\n")
print(":::::::::::::::::::::::::  :         results processing:")

# Call the functions to retrieve the information
get_processor_info()
get_processing_units_info()
print("\n")

def discover_devices(ip_range):
    devices = []
    try:
        ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=False)
        for _, packet in ans:
            devices.append((packet[ARP].psrc, packet[Ether].src))
    except Exception as e:
        print(f"An error occurred while discovering devices: {e}")
    return devices


def measure_speed():
    try:
        st = Speedtest()
        download_speed = st.download() / 10**6  # Convert to Mbps
        upload_speed = st.upload() / 10**6  # Convert to Mbps
        return download_speed, upload_speed
    except Exception as e:
        print(f"An error occurred while measuring speed: {e}")
        return None


def main():
    # Specify the IP range to scan (e.g., "192.168.1.0/24")
    ip_range = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.0/24"

    # Discover devices
    devices = discover_devices(ip_range)
    print(f"Devices connected to the router ({ip_range}):")
    for ip, mac in devices:
        print(f"IP: {ip}\tMAC: {mac}")

    # Measure speed
    speed_result = measure_speed()
    if speed_result:
        download_speed, upload_speed = speed_result
        print(f"\nInternet Speed:")
        print(f"Download: {download_speed:.2f} Mbps")
        print(f"Upload: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    main()
