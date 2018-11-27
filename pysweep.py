#!/usr/bin/env python

import subprocess
import ipaddress
import re

iplist = []

def main():
    target_ip = input("Enter IP or CIDR: ")

    cidr = ipaddress.ip_network(target_ip)
    
    outputList = []
    for x in cidr:
        y = "fping -a -C 5 -q " + str(x)
        outputList.append(subprocess.getstatusoutput(y))

    with open("output.txt", "w+") as file:
            for x in outputList:
                    file.write(str(x).strip("'") + "\n")
    file.close()
    
    output = open("output.txt", "r")

    onoff = []
    ip = []
    col = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    num_lines = 0
   
    for evrline in output:
        if re.match(r"\([1]{1}(.*)\n", evrline):
                num_lines += 1
                fields = evrline.split(' ')
                field1 = fields[0] #1
                field2 = fields[1] #IP
                field3 = fields[2] #:       
                field4 = fields[3] #T1
                field5 = fields[4] #T2
                field6 = fields[5] #T3
                field7 = fields[6] #T4
                field8 = fields[7] #T5
                onoff.append(field1)
                ip.append(field2)
                col.append(field3)
                t1.append(field4)
                t2.append(field5)
                t3.append(field6)
                t4.append(field7)
                t5.append(field8)  

    for a, b, c, d, e, f in zip(ip, t1, t2, t3, t4, t5):
            print("Host: " + (a).strip("'") + " is detected online. Response time(s) were: " + b + " " + c + " " + d + " " + e + " " + f)
    print("The following hosts were found to be online and responding to ping requests:")
    print("Detected Hosts:")
    print("================")
    for eachip in ip:
            print(eachip.strip("'")) 

if __name__== '__main__':
        main()