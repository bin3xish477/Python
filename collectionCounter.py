#!/usr/bin/env python3
from sys import argv
from re import findall
from collections import Counter

FILE = argv[1]

def main():
    log = open(FILE, 'r').read()
    ipList = findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', log)
    # A container object that returns a dictionary with 
    # the unique items in an iterable and the number of times it appears.
    uniqIpList = Counter(ipList)
    for IP in ipList:
        print(IP, uniqIpList[IP])

if __name__ == '__main__':
    main()