import threading
from sys import exit

def create_threads(username, password, cmd_list, ip_list, func):
	""" create threads for concurrent connections 
	
	Args:
		username (str): the username of the user.
		password (str): the password for the user specified.
		cmd_list (list): list containing the commands to run on switch.
		ip_list (list): list containing target IP addresses.
		func (function): function to assign to each thread.
	"""
	threads = []
	for ip in ip_list:
		th = threading.Thread(
			target=func, args=(username, password, cmd_list, ip,)
		)
		th.start()
		threads.append(th)

	for thread in threads:
		thread.join()