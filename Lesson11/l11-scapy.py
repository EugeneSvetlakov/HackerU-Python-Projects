"""
ip scaner for local IPs
run: sudo python3 l11-scapy.py -r "192.168.1.0/24" -i "eth0"
"""
import scapy.all as scapy

import argparse
from scapy.layers.l2 import Ether, ARP
# from scapy.layers.inet import IP


# scapy.IP
def args():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument(
        "-r", "--range", required=False,
        help="IP/Netw to scan", default="192.168.1.0/24")
    parser.add_argument(
        "-i", "--interface", required=False,
        help="interface name (e.g. eth0", default="eth0")
    return parser.parse_args()


def scan(ips, ilink):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ips)  # 192.168.1.1/24
    p = broadcast / arp
    ans, _ = scapy.srp(p, timeout=3, verbose=False, iface=ilink, intr=0.5)
    # [(s,r),(s,r),(s,r)]
    res = []
    for s, r in ans:
        res.append(f"IP:{r.psrc} MAC:{r.hwsrc}")
    return res


def show_res(res):
    for s in res:
        print(s)


if __name__ == '__main__':
    options = args()
    res = scan(options.range, options.interface)
    show_res(res)
