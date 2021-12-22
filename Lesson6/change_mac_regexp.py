#!./venv/bin/python3
import subprocess
import argparse
import re
import random

# Links:
# [regex online](https://regex101.com/)

# mac = "02:a2:f0:bb:10:a2"

def get_random_mac():
    first = random.randint(0, 255)
    first = first + 1 if first % 2 else first
    mac = ":".join(["{:0>2.2}".format(hex(random.randint(0, 15)).replace("0x", "")) for _ in range(5)])
    return "{:0>2.2}".format(hex(first).replace("0x", "")) +":" + mac


def check_input_mac(mac):
    return re.match(r"^([0-9a-f]{2}[:-]?){5}[0-9a-f]{2}", mac.lower())


def args():
    parser = argparse.ArgumentParser("this is my awesome script to change mac")
    parser.add_argument("-m", "--mac", help="mac address to change to", default="r")
    parser.add_argument("-i", "--iface", help="interface", required=True)
    return parser.parse_args()


def change_mac(mac, iface):
    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig", iface, "hw", "ether", mac])
    subprocess.call(["ifconfig", iface, "up"])


def check_result(mac, iface):
    res = subprocess.check_output(["ifconfig", iface]).decode()
    if mac in res:
        print("[+] mac changed")
    else:
        print("[-] something goes wrong")


if __name__ == '__main__':
    options = args()
    mac = options.mac
    if mac == "r":
        mac = get_random_mac()
    if not check_input_mac(mac):
        print("[-] wrong mac format, exit")
        exit(0)
    change_mac(mac, options.iface)
    check_result(mac, options.iface)
