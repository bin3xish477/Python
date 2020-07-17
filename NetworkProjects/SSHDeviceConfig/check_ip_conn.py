from sys import exit
from subprocess import run, DEVNULL
from platform import system

def check_ip_conn(ip_list):
	""" Checks if all IP's are pingable.
	
	Args:
		ip_list (list): list containing IP addresses to be pinged.
	"""
	os = system()

	for ip in ip_list:
		# checking operating and running ping command accordingly
		if os == "Windows":
			ping_reply = run(["ping", "-c", "2", ip], stdout=DEVNULL, stderr=DEVNULL)
		if os == "Linux":
			ping_reply = run(["ping", ip, "/n", "2"], stdout=DEVNULL, stderr=DEVNULL)

		# if exit status code is not equal 0, the ip was unreachable - exit program
		if ping_reply != 0:
			print(f"[-] {ip} is unreachable...")
			exit(1)
	print("[+] All IP's are reachable...")
