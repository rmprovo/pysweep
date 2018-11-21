#!/usr/bin/env python

import subprocess
import ipaddress
import re

iplist = []


def main():
    target_ip = input("Enter IP or CIDR: ")

    ucodeip = (target_ip)

    cidr = ipaddress.ip_network(ucodeip)

    output = []
    for x in cidr:
        y = "fping -a -C 5 -q " + str(x)
        output.append(subprocess.getstatusoutput(y))
                
    ip1 = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    num_lines = 0

    for evrline in output:
        if re.match("(1(.*))", evrline):
                num_lines += 1
                fields = evrline.split(" ")
                field1 = fields[0] #1
                p1.appd = fields[1] #IP
                field3 = fields[2] #:       
                t1.append = fields[3] #T1
                t2.append = fields[4] #T2
                t3.append = fields[5] #T3
                t4.append = fields[6] #T4
                t5.append = fields[7] #T5
                
    print(ip1)

if __name__== '__main__':
        main()
    





