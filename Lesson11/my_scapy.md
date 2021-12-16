# Scapy

## Links:
[link 1](https://scapy.readthedocs.io/en/latest/)
[link 2](https://habr.com/ru/post/208786/)

## ДЗ: В виртуалке: Отработать скрипты, настроить ip_forwarding

## 
ls()
ls(TCP) - list TCP protocol 
help(sr) - get help

## IP
p_ip = IP()
p_ip
p_ip.summary()
p_ip.show()
p_ip = IP(dst="empty.jack.ru")
p_ip.src
p_ip.show()
ls(p_ip)

## TCP
p_tcp = TCP()
p_tcp.show()
p_tcp = TCP(dport=22)

## create tcp packer
p = p_ip / p_tcp / "hello"
send(p) # simple send packer
ans = sr1(p) # send 1 packer and recieve answer
p[TCP]  or p["TCP"]
p.haslayer("ARP")
p.getlayer("ARP")
p.getlayer("TCP")

##
p_ip_range = IP(dst="192.168.25.0/24")
p_port_range = TCP(dport=(1,500))

## send packets for port range
p_ip = IP(dst="45.143.93.4")
p = p_ip/p_port_range
ans, uns = sr(p, timeout=3)
unsac
ans
ans[0]
ans.summary()
ans.nsummary()
print(*filter(lambda t:t[1][TCP].flags=="SA",ans),sep="\n")
ans.summary(lfilter=lambda s,r:r[TCP].flags=="SA")
list(ans.filter(lambda s,r:r[TCP].flags=="SA"))

## sniff
sniff(prn=lambda p: p.summary())

## scan lan by ARP
p = Ether()/ARP(pdst="192.168.5.0/24")
help(srp)
help(srp1)
ans, _ = srp(p, timeout=3)

## python script using scapy
import scapy.all as scapy