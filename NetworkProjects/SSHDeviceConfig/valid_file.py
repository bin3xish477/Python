from os import path
from sys import exit

def valid_file(file_name):
	"""Checks if the provided destination file exist.
	
	Args:
		file_name (str): name of file to validate.
	"""
	abs_path = path.abspath(file_name)
	print(f"\n\u2022 Path to file: \033[01m{abs_path}\033[0m")

	if (
		not path.exists(abs_path) and not path.isfile(abs_path)
	):
		print("\u203c File not found or does not exists...")
		exit(1)
	print("\u2192 File has been verified...\n")

	file_content = open(file_name, "r")
	file_content.seek(0)
	file_content = file_content.readlines()

	return file_content
