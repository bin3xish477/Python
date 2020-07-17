import paramiko
from sys import exit
from os import path
from time import sleep
from re import search
from get_prog_info import get_prog_info
from valid_ips import valid_ips
from check_ip_conn import check_ip_conn

def ssh_conn(username, password, cmd_list, target_ip):
	""" Creates SSH connection to target IP and
	runs command on the target Arista switch.

	Args:
		username (str): the username of the user.
		password (str): the password for the user specified.
		cmd_list (list): list containing the commands to run on switch.
		target_ip (str): the IP address of the target switch.
	"""
	try:
		# creating an SSH session with paramiko.
		session = paramiko.SSHClient()
	except paramiko.AuthenticationException:
		print("\u203c username or password is incorrect...")

def main():
	username, password, cmd_list, ip_list = get_prog_info()

	# verify that each IP in ip_list is in a valid IP format.
	valid_ips(ip_list)
	# check if every IP address is pingable.
	check_ip_conn(ip_list)

	# connect to target IP and run commands on switch.
	for ip in ip_list:
		ssh_conn(username, password, cmd_list, ip)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit(1)
