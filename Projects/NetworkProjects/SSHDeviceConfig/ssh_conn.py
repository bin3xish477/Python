import paramiko
from sys import exit
from os import path
from time import sleep
from re import search
from get_prog_info import get_prog_info
from valid_ips import valid_ips
from check_ip_conn import check_ip_conn
from create_threads import create_threads

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
		# for testing purposes, this allows auto-accepting unknown host keys
		# do not use in production! The default would be RejectPolicy
		session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		# connect to the switch using username and password
		session.connect(target_ip.strip(), username=username, password=password)
		# start in interactive session with the switch
		conn = session.invoke_shell()
		# setting default modes on switch
		conn.send("enable\n")
		conn.send("terminal length 0\n")
		sleep(1)

		# send the user commands to the switch
		for cmd in cmd_list:
			conn.send(cmd+"\n")
			sleep(2)

		# receiving data back from switches
		resp = conn.recv(65535)
		print(f"\u2022 Response from \u2192 {target_ip}")
		print(str(resp)[2:-1]+"\n")

		session.close()
	except paramiko.AuthenticationException:
		print(" \u203c username or password is incorrect...")
		exit(1)

def main():
	username, password, cmd_list, ip_list = get_prog_info()
	# verify that each IP in ip_list is in a valid IP format.
	valid_ips(ip_list)
	# check if every IP address is pingable.
	check_ip_conn(ip_list)
	# call function to create concurrent ssh connections
	create_threads(username, password, cmd_list, ip_list, ssh_conn)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit(1)
