# Scapy

## Links:
[link 1](https://scapy.readthedocs.io/en/latest/)
[link 2](https://habr.com/ru/post/208786/)


## Install
### Only scapy
pip install scapy
### scapy and IPython. Hightly recommended
pip install --pre scapy[basic]
### scapy and all its main dependencies
pip install --pre scapy[complite]
### Platform-specific instructions
sudo apt-get install tcpdump

## scapy in python:
import scapy.all as scapy

## discover the Scapy layers and protocols
explore()
## Type help() for interactive help, or help(object) for help about object.
help(sr) - get help
## List  available layers, or infos on a given layer class or name.
ls()
### list TCP protocol
ls(TCP)
### Displays Scapy's default commands
lsc()
## get latest result: _ (underscore)
_

## configuration
### get default interface
conf.iface
## IP
p_ip = IP()
p_ip = IP(dst="127.0.0.1")
p_ip
p_ip.summary()
p_ip.show()
p_ip.dst
p_ip.src
p_ip.ttl
p_ip.show()
ls(p_ip)
### ip range
ip_range = IP(dst=["192.168.1.1", "192.168.10.0/28"], ttl=(1, 9))
[p for p in ip_range]
ip_range = IP(dst=["192.168.1.1", "192.168.10.2"], ttl=[1, 2, (5, 9)])
[p for p in ip_range]
ip_range = IP(dst="192.168.25.0/24")
[p for p in ip_range]
ip_range = IP(dst="host.rodina-test.lan/32")
[p for p in ip_range]
ip_range = IP(dst="host.rodina-test.lan/30")
[p for p in ip_range]
ip_range = IP(dst="host.rodina-test.lan/28")
[p for p in ip_range]
ip_range = IP(dst="host.rodina-test.lan/24")

## TCP
p_tcp = TCP()
p_tcp.show()
p_tcp = TCP(dport=22)
p_tcp = TCP(dport=[80, 443])
p_tcp = TCP(dport=[80, 443, (21,25)])

### port range
port_range = TCP(dport=(1,500))


## Packerts
### packets and TCPIP layers
IP()
IP()/TCP()
Ether()/IP()/TCP()
Ether()/IP()/TCP()/"GET / HTP/1.0\r\n\r\n"
Ether()/IP()/IP()/UDP()
IP(proto=55)/TCP()
### work with packer
#### create
p_ip = IP(dst="192.168.1.1")
p_icmp = ICMP()
p = p_ip / p_tcp
#### Обращение к элементам пакета
p[ICMP]
p["TCP"]
p[IP].dst
p.haslayer(ARP)
p.haslayer(ICMP)
p.getlayer(ARP)
p.getlayer("IP")
#### send packet
##### L3 layer
send(p) # simple send packer
> В терминале запустить 'sudo tcpdump -nn -vv -i any port not 22'
###### sr1() - send packets at layer 3 and return only first answer
ans = sr1(p, timeout=2)
ans
ans.show()
sr1(IP(dst="192.168.1.1")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.yandex.ru")))

###### sr() - Send and receive packets at layer 3
> They return a couple of two lists. The first element is a list of couples (packet sent, answer), and the second element is the list of unanswered packets.
> If there is a limited rate of answers, you can specify a time interval (in seconds) to wait between two packets with the inter parameter.
> If some packets are lost or if specifying an interval is not enough, you can resend all the unanswered packets, either by calling the function again, directly with the unanswered list, or by specifying a retry parameter.
> If retry is 3, Scapy will try to resend unanswered packets 3 times. If retry is -3, Scapy will resend unanswered packets until no more answer is given for the same set of unanswered packets 3 times in a row. The timeout parameter specify the time to wait after the last packet has been sent:
sr(IP(dst="192.168.1.1")/TCP(dport=[21,22,23]))
range_ip = [p for p in IP(dst=["192.168.1.1", "192.168.2.0/28"])]
range_port = [p for p in TCP(dport=[22,80,(440,443)])]
ip = IP(dst=["192.168.1.1", "192.168.2.0/28"])
port = TCP(dport=[22,80,(440,443)])
range_packer = [p for p in ip/port]
sr(IP(dst="192.168.1.1")/TCP(dport=[21,22,23]), inter=0.5, retry=)
ans, unans = sr(IP(dst="192.168.1.1-2")/TCP(dport=[21,22,245]), inter=0.5, retry=2, timeout=1)
> resend unanswered packets:
sr1(unans, timeout=1)
> Просмотр результатов
unans
ans
ans[0]
ans[2]
ans[TCP].show()
ans[UDP].show()
ans[TCP][1][0] # sended part on second TCP packet
ans[TCP][1][1] # recieved part on second TCP packet
ans.nsummary()
ans.summary()
ans.summary(lambda s,r: s.sprintf("%TCP.sport% \t %IP.dst%"))
ans.summary(lambda s,r: s.sprintf("%TCP.sport% \t %IP.dst%")+r.sprintf("\t %TCP.flags%"))
print(*filter(lambda t: t[1][TCP].flags=="RA", ans), sep="\n")
print(*filter(lambda t: t[0][TCP].flags=="S", ans), sep="\n")
ans.summary(lfilter=lambda s,r:r[TCP].flags=="RA")
ans.summary(lfilter=lambda s,r:r[TCP].flags=="RA", prn=lambda s,r: (s[IP].dst), s[TCP].dport))
list(unans)
list(ans.filter(lambda s,r:r[TCP].flags=="SA").show(lambda s,r: (s[IP].dst, s[TCP].dport)))
list(unans.filter(lambda s:s[TCP].dport==22))
ans.make_table(lambda s,r:(r[IP].dst, r[TCP].sport, "X"))

##### L2 layer
###### sendp()
> отправляет пакеты, используя канальный (L2) уровень,
> учитываются указанные параметры и заголовки Ethernet кадров.
> Ответы всё так же не ожидаются и не обрабатываются;
p = Ether()/ARP(pdst="192.168.5.0/24")
sendp(p)
###### srp1()
> аналогично sr1(), только уже канальный уровень.

###### srp()
> отправляет и принимает пакеты, уровень L2
packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = "192.168.1.0/24")
ans, unans = srp(packet, timeout = 2, iface = "eth0", inter = 0.1)
> timeout – укажет, сколько времени (в секундах) нужно ждать до получения ответного пакета, retry – сколько раз нужно повторно слать пакет, если ответ не был получен и одна из самых полезных опций – это filter, синтаксис которого очень похож на tcpdump.
packet = IP(dst="192.168.1.1")/TCP(dport=[23, 80],flags="S")
ans, unans = srp(packet, timeout = 2, filter="host 192.168.1.242 and port 23", iface = "eth0", inter = 0.1)
ans, unans = sr(packet, timeout = 2, filter="host 192.168.1.242 and port 23", iface = "eth0", inter = 0.1)
### SYN Scans
sr1(IP(dst="192.168.1.1")/TCP(dport=80,flags="S"), timeout=2)
> Use either notations to scan ports 400 through 443 on the system::
sr(IP(dst="192.168.1.1")/TCP(sport=666, dport=(400,443),flags="S"), timeout=2)
ans, unans = sr(IP(dst="192.168.1.1")/TCP(sport=RandShort(), dport=(400,443),flags="S"), timeout=2)
ans.summary()
ans.summary(lambda s,r: s.sprintf("%TCP.sport% \t %IP.dst%"))
ans.make_table(lambda s,r:(s[IP].dst, r[TCP].sport, r.sprintf("%flags%")))
ans, unans = sr(IP(dst=["192.168.1.1", "192.168.1.247"])/TCP(sport=RandShort(), dport=[22,80,443],flags="S"), timeout=3, retry=2)
ans.make_table(lambda s,r:(s[IP].dst, r[TCP].sport, r.sprintf("%flags%")))
## sniff
> We can easily capture some packets or even clone tcpdump or tshark. Either one interface or a list of interfaces to sniff on can be provided. If no interface is given, sniffing will happen on "conf.iface"
> 
conf.iface
pkt_dump = sniff(filter="icmp and host 192.168.1.1", count=2)
pkt_dump.summary()
pkt_dump = sniff(iface="lo", count=2)
sniff(iface="eth1", prn=lambda x: x.show(), count=3)
sniff(prn=lambda p: p.summary(), count=3)
pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"), count=3)
> passive OS fingerprinting:
load_module("p0f")
a=sniff(prn=prnp0f)
> Ti show interface on whitch packer recieved use argument 'sniffed_on'
sniff(iface=["lo", "eth0"], prn=lambda x: x.sniffed_on+": "+x.summary(), count=4)
## scan lan by ARP
p = Ether()/ARP(pdst="192.168.5.0/24")
help(srp)
help(srp1)
ans, _ = srp(p, timeout=3)

## Reading PCAP files
a=rdpcap("/spare/captures/isakmp.cap")
a
## python script using scapy
import scapy.all as scapy