#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface= interface, store=False, prn=process_sniffed_packet) # prn is to call the function every time sniff executes

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):

            print(packet[scapy.Raw].load)

sniff('eth0')