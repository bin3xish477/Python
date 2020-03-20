#!/usr/bin/env python3
from sys import argv
import re
import subprocess as subp
FILE = argv[1]
def auth_parser():
	print('-------------------------------------')
	print('| Percent | Count |              IP |')
	print('-------------------------------------')
	with open(FILE, 'r') as auth_file:
		TOTAL = 0
		data = auth_file.read()
		ip_addrs = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", data)
		set_ip = set(ip_addrs)
		set_ip.remove('0.0.0.0')
		TOTAL = len(ip_addrs) - 2
		IP_COUNT = len(set_ip)
		my_dict = {ip: 0 for ip in ip_addrs if ip != '0.0.0.0'}
		for p in set_ip:
			for ip in ip_addrs:
				if ip == p:
					my_dict[p] += 1
	# math stuff
	for ip, val in my_dict.items():
		percen = (my_dict[ip] * 100) / TOTAL
		if percen > 9:
			print(str((f'|  {percen:.3f} ')) + '|' + str(my_dict[ip]).rjust(7) + '|' + ip.rjust(17) + '|')
		else:
			print(str((f'|  {percen:.4f} ')) + '|' + str(my_dict[ip]).rjust(7) + '|' + ip.rjust(17) + '|') 
	print('-------------------------------------')
	print('|   Total |   ' + str(TOTAL) + '|                 |')
	print('-------------------------------------')
if __name__ == '__main__':
	auth_parser()
