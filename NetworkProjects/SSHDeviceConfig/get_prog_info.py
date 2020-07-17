from sys import exit
from getpass import getpass
from valid_file import valid_file

def get_prog_info():
	""" Prompt user for username and password to Arista switches
	and name of file in the current path containing commands
	to execute on Arista switches.
	"""
	username = input("\u2022 Enter username: ")
	password = getpass(prompt="\u2022 Enter password: ")

	command_file = input("\u2022 Enter name of file containing commands (Ex. cmd.txt): ")
	ip_file = input("\u2022 Enter name of file containing commands (Ex. ip.txt): ")
	commands = valid_file(command_file)
	ip_list = valid_file(ip_file)

	return username, password, commands, ip_list
