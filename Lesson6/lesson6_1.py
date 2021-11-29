import subprocess
import argparse


def get_ip_links(linkname):
    subprocess.call(["ip", "link", "show", linkname])


def args():
    parser = argparse.ArgumentParser("this is my awesome script to change mac")
    parser.add_argument(
        "-m", "--mac", help="mac address to change", required=True)
    parser.add_argument("-i", "--iface", help="interface", default="eth0")
    return parser.parse_args()


if __name__ == '__main__':
    prog_option = args()
    print("mac: ", prog_option.mac)
    print("iface: ", prog_option.iface)
    get_ip_links(prog_option.iface)
