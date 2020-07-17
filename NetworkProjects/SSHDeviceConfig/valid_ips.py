from re import search
from sys import exit

def valid_ips(ip_list):
	""" Verify that said IP are valid.
	
	Args:
		ip_list (list): list containing IP addresses for validation.
	"""
	for ip in ip_list:
		if len(re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip.strip()) == 0:
			print("[-] Found an invalid IP address...")
			exit(1)
	print("[+] All IP addresses have been successfully validated...")
