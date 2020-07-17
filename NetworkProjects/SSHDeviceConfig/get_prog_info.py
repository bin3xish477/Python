from sys import exit
from getpass import getpass
from valid_file import valid_file

def get_prog_info():
	""" Prompt user for username and password to Arista switches
	and name of file in the current path containing commands
	to execute on Arista switches.
	"""
	username = input("[+] Enter username: ")
	password = getpass(prompt="[+] Enter password: ")

	command_file = input("[+] Enter name of file containing commands (Ex. cmd.txt): ")
	commands = valid_file(command_file)

	return username, password, command_file
