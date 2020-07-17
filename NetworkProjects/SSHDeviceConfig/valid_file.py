from os import path
from sys import exit

def valid_file(file_name):
	"""Checks if the provided destination IP file exist.
	
	Args:
		file_name (str): name of file containing IP addresses to connect to.
	"""
	abs_path = path.abspath(file_name)
	print(f"[+] Path to file:\n{abs_path}")

	if (
		not path.exists(abs_path) and not path.isfile(abs_path)
	):
		print("[-] File not found or does not exists...")
		exit(1)
	print("[-] File has been verified...")

	ip_file = open(file_name, "r")
	ip_file.seek(0)
	ip_list = ip_file.readlines()

	return ip_list
