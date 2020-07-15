import os.path
import sys.exit

def valid_file(file_name):
	"""Checks if the provided destination IP file exist
	
	Args:
		file_name (str): name of file containing IP addresses to connect to.
	"""

	if not exists(file_name) and not isfile(file_name):
		print("[-<] File not found or does not exists...")
		exit(1)
	print("[->] File has been verified...")

	ip_file = open(file_name, "r").seek(0).readlines()
	return ip_file

