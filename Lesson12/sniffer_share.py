"""
some doc
"""
import scapy.all as scapy
import argparse
# from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTPRequest, HTTP, Raw, HTTPResponse
from scapy.packet import Packet


def args():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("-s", "--site", help="host to sniff", default=None)
    return parser.parse_args()

ban = [".png",".gif",".ico"]
def packet_analyse(packet: Packet):
    # print(p.summary())
    # if packet.getlayer("IP").src != "10.0.2.4" or packet.getlayer("IP").dst != "10.0.2.4":
    #     return


    if packet.haslayer(HTTPRequest):
        path = packet[HTTPRequest].Path.decode('utf-8')
        host = packet[HTTPRequest].Host.decode('utf-8')
        for ext in ban:
            if ext in path:
                return
        print("-" * 120)
        print("src IP:", packet[IP].src)
        print("dst IP:", packet[IP].dst)
        url = "http://" + host + path
        print("url:", url)
        # print(packet.show())
        if packet.haslayer(scapy.Raw):
            # print("raw.load:", packet[scapy.Raw].show())
            try:
                print(packet[scapy.Raw].load.decode())
            except:
                pass
            # hexdump(packet[scapy.Raw].load)
    elif packet.haslayer(HTTPResponse):
        # path = packet[HTTPResponse].Path.decode('utf-8')
        # host = packet[HTTPResponse].Host.decode('utf-8')
        # for ext in ban:
        #     if ext in path:
        #         return
        print(packet[HTTPResponse].show())
        print("-" * 120)
        print("src IP:", packet[IP].src)
        print("dst IP:", packet[IP].dst)
        # url = "http://" + host + path
        # print("url:", url)
        # print(packet.show())
        if packet.haslayer(scapy.Raw):
            # print("raw.load:", packet[scapy.Raw].show())
            try:
                print(packet[scapy.Raw].load.decode())
            except:
                pass
            # hexdump(packet[scapy.Raw].load)


if __name__ == '__main__':
    options = args()
    if options.site:
        scapy.sniff(prn=packet_analyse, filter=f"port 80 and host {options.site}", session=scapy.TCPSession)
    else:
        scapy.sniff(prn=packet_analyse,filter=f"port 80", session=scapy.TCPSession)

"""
some doc
"""
import scapy.all as scapy
import argparse
# from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTPRequest, HTTP, Raw
from scapy.packet import Packet


def args():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("-s", "--site", help="host to sniff", default=None)
    return parser.parse_args()

ban = [".png",".gif",".ico"]
def packet_analyse(packet: Packet):
    # print(p.summary())
    # if packet.getlayer("IP").src != "10.0.2.4" or packet.getlayer("IP").dst != "10.0.2.4":
    #     return


    if packet.haslayer(HTTPRequest):
        path = packet[HTTPRequest].Path.decode('utf-8')
        host = packet[HTTPRequest].Host.decode('utf-8')
        for ext in ban:
            if ext in path:
                return
        print("-" * 120)
        print("src IP:", packet[IP].src)
        print("dst IP:", packet[IP].dst)
        url = "http://" + host + path
        print("url:", url)
        # print(packet.show())
        if packet.haslayer(scapy.Raw):
            # print("raw.load:", packet[scapy.Raw].show())
            try:
                print(packet[scapy.Raw].load.decode())
            except:
                pass
            # hexdump(packet[scapy.Raw].load)


if __name__ == '__main__':
    options = args()
    if options.site:
        scapy.sniff(prn=packet_analyse, filter=f"port 80 and host {options.site}", session=scapy.TCPSession)
    else:
        scapy.sniff(prn=packet_analyse,filter=f"port 80", session=scapy.TCPSession)


