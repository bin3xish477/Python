#!/usr/bin/env python3
"""
Chrome Web Driver Zip File
https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip
"""

from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from pathlib import Path
from platform import system
from time import sleep
from os import devnull
from sys import exit
from json import loads


def start_chrome(path_to_driver, headless=True):
	options = ChromeOptions()

	# Setting headless options to false to ensure
	# browser will not run in background
	if headless:
		options.add_argument("headless")
	options.add_argument('log-level=3')

	# Starting browser with specified options and sending all logs to null file
	driver = Chrome(executable_path=path_to_driver, options=options)
	
	return driver
	
def open_learndot_tab(driver, url, email=None, passwd=None, prompt_login=False):
	# Prompt user for login creds before spawning learndot login tab
	# if no email and password was not supplied as program arguments
	if prompt_login:
		def login():
			email = input("Enter LearnDot email: ")
			passwd = getpass("Enter LearnDot Password: ")
			return (email, passwd)
		email, passwd = login()

	# Open tab to learndot login page
	driver.get(url)

	# Getting email input field element
	email_input = driver.find_element_by_name("email")
	sleep(0.5)

	# Send email and press enter
	email_input.send_keys(email, Keys.ENTER)

	# Get password input field element
	passwd_input = driver.find_element_by_name("password")
	sleep(0.5)
	
	# Send password and press enter
	passwd_input.send_keys(passwd, Keys.ENTER)
	

def create_office_hours(driver, values: dict):
	for i in range(values["dates"]):
		# Get description element
		description = driver.find_element_by_name("description")
		sleep(0.5)
		
		# Input description into description element
		description.send_keys(values["description"], Keys.ENTER)

		# Select location element
		office_hours_location = driver.find_element_by_name("location")
		sleep(0.5)

		# Set location value
		office_hours_location.send_keys(values["location"], Keys.ENTER)

		# Get Date selection field
		date_selector = driver.find_elements_by_class_name("react-datepicker-wrapper")

		# Set date value
		date_selector.send_keys(values["dates"][i], Keys.ENTER)

		# Pause the program and wait after submitting office hours form
		# before filling out another one
		sleep(2)

def arg_parse():
	from argparse import ArgumentParser
	parser = ArgumentParser()
	parser.add_argument("-e", "--email", help="LearnDot Email")
	parser.add_argument("-p", "--passwd", help="LearnDot Password")
	parser.add_argument("-s", "--show-gui", action="store_true", help="Show Browser Window GUI")
	return parser.parse_args()


def main():
	# Parse programs arguments
	args = arg_parse()

	# Check if all arguments have been properly set
	if args.show_gui:
		if not args.email or not args.passwd:
			print("[ERROR] If `-s` argument is used, must pass arguments `-e` and `-p`")
			exit(1)
		headless = False
	headless = True

	# Get operating system
	system_ = system()

	# Get users home directory
	user_home_dir = str(Path.home())

	# Get absolute path to chrome driver
	if system_ == "Windows":
		path_to_driver = user_home_dir + "\\Documents\\chromedriver.exe"
	else:
		path_to_driver = user_home_dir + "/Documents/chromedriver.exe"

	# Start the chome driver
	driver = start_chrome(path_to_driver, headless=headless)
	
	# Office hours creation link
	url = "https://learn.fullstackacademy.com/officehours/form/add"

	if args.show_gui:
		# Option tab and go to the office hour creation page
		open_learndot_tab(driver, url, args.email, args.passwd)
	else:
		open_learndot_tab(driver, url, prompt_login=True)
	
	with open("values.json", "r") as f:
		# Load JSON values from file in a Python Dictionary
		values = loads(f)

		# Call function to create office hours
		create_office_hours(driver, values=values)

	# Close chrome driver
	driver.quit()


if __name__ == "__main__":
		main()