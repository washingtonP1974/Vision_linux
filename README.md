# Vision_linux

List of active processes, processor and internet information.

With this tool, obtain an in-depth search of information about the processor and processing units in the list.
In this same Python script that uses the scapy library to discover devices connected to a router, measures your internet speed using speedtest-cli library and identify hosts.
The script will check the specified IP range, discover devices connected to the router, display your IP and MAC addresses and measure the internet speed using the speedtest-cli library.

First, make sure you have the scapy and speedtest-cli libraries installed.
You can install them using pip:


1) sudo apt-get install speedtest

Better information (speedtest-cli) https://www.speedtest.net/pt/apps/cli

2) chmod a+x vision.py

4) python3 vision.py 192.168.1.0/24

or

python3 vision.py 192.168.x.x (192.168.x.x = your router's ip - eth0 or wlan0)
