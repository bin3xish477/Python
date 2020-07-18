from re import search
from sys import exit

def valid_ips(ip_list):
	""" Verify that said IP are valid.
	
	Args:
		ip_list (list): list containing IP addresses for validation.
	"""
	for ip in ip_list:
		found_ip = search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ip.strip())
		try:
			found_ip.group(0)
		except AttributeError:
			print(f" \u203c Found an invalid IP address: {ip}")
			exit(1)
	print(" \u2192 All IP addresses have been successfully validated...")
