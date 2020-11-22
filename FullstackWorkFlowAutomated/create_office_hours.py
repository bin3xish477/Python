#!/usr/bin/env python3

"""
Chrome Web Driver Zip File
https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip
"""

from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from getpass import getpass
from pathlib import Path
from platform import system
from time import sleep
from os import environ
from sys import exit
from json import load
from colored import fg, attr
from datetime import datetime, date


def start_chrome(path_to_driver):
	# Will allow us to specify options for our chromedriver
	options = ChromeOptions()

	# Turn off logging
	options.add_argument('log-level=3')

	# Start browser in full screen mode
	options.add_argument("start-maximized")

	# Starting browser with specified options and sending all logs to null file
	driver = Chrome(executable_path=path_to_driver, options=options)
	
	return driver


def open_learndot_tab(path_to_driver, url, email=None, passwd=None):
	# Start the chome driver
	print("[%sATTENTION%s] Launching browser ..." % (fg(65), attr(0)))
	driver = start_chrome(path_to_driver)

	# Open tab to learndot get_login page
	driver.get(url)
	sleep(3)

	#try:
	# Getting email input field element
	email_input = driver.find_element_by_xpath("/html/body/div/div/welcome-dot/div/login/div/form/div[1]/input")

	# Send email and press enter
	email_input.send_keys(email, Keys.ENTER)

	# Get password input field element
	passwd_input = driver.find_element_by_xpath("/html/body/div/div/welcome-dot/div/login/div/form/div[1]/div[2]/input")
	
	# Send password and press enter
	passwd_input.send_keys(passwd, Keys.ENTER)
	#except:
	#	print("[%sFATAL%s] login was unsuccessful... try again and make sure your credentials are valid" % (fg(196), attr(0)))
	#	exit(1)

	return driver
	

def create_office_hours(driver, url, values: dict):
	sleep(4)
	for i in range(len(values["dates"])):
		try:
			# Get description element
			description = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/input[1]")

			# Input description into description element
			description.send_keys(values["description"], Keys.TAB)

			# Select location element
			office_hours_location = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/input[2]")

			# Set location value
			office_hours_location.send_keys(values["location"], Keys.TAB)

			# Get Date selection field
			date_setter = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/input")

			# Set date value
			date_setter.send_keys(Keys.CONTROL + 'a')
			date_setter.send_keys(values["dates"][i], Keys.ENTER)

			# Get Date selection field
			hour_setter = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/input[1]")

			# Set Hour
			hour_setter.send_keys(Keys.CONTROL + 'a')
			hour_setter.send_keys(values["time"]["hour"], Keys.ENTER)

			# Get Date selection field
			minute_setter = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/input[2]")

			# Set Minute
			minute_setter.send_keys(Keys.CONTROL + 'a')
			minute_setter.send_keys(values["time"]["minute"].zfill(2), Keys.ENTER)

			# Get am/pm field 
			am_pm_setter = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/button")
			if am_pm_setter.text == "AM" and values["time"]["am_pm"].upper() == "AM":
				pass	
			else:
				am_pm_setter.send_keys(Keys.ENTER, Keys.TAB)

			# Get num of slots field
			num_of_slots = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/input[3]")

			# # Set number of slots value
			num_of_slots.send_keys(Keys.CONTROL + 'a')
			num_of_slots.send_keys(values["num_of_slots"], Keys.ENTER)

			# # Get slot duration field
			slot_duration = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/input[4]")

			# # Set duration value
			slot_duration.send_keys(Keys.CONTROL + 'a')
			slot_duration.send_keys(values["slot_duration"], Keys.ENTER)
			
			# Get booking method field
			booking_method_selector = Select(driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/select"))

			# Selecting booking method value
			booking_method = values["booking_method"].strip().lower()
			if booking_method == "any available":
				booking_method_selector.select_by_value('0')
			elif booking_method == "sequential booking":
				booking_method_selector.select_by_value('1')
			else:
				booking_method_selector.select_by_value('-1')

			# Set employee only field
			if values["employees_only"]:
				driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/label[6]/input").click()
			
			# Get restrict to field
			restrict_to_cohort = driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[2]/div[1]/input")
			
			# Set restrict cohort values
			for cohort in values["restrict_to_cohorts"]:
				restrict_to_cohort.send_keys(cohort[:-1])
				sleep(1)
				driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[2]/div[1]/div/ul/li").click()

			# Create session		
			driver.find_element_by_xpath("/html/body/div[2]/ui-view/ui-view/div/div/div/div[2]/div[2]/div[3]/button[2]").click()
		except:
			print(
				"[%sFATAL%s] Something went wrong... try checking your values.json files to see if there are any invalid values"
				% (fg(196), attr(0))
			)
			exit(1)

		# Once we create the last office hour session break
		# the loop as opposed to reopen the create session page
		if i == len(values["dates"]) - 1:
			break
		else:
			driver.get(url)
			sleep(3)


def get_login(from_env=False):
	# If email and password are set as environment variables, read
	# use those creds as valid creds for learndot
	if from_env:
		"""
		Setting environment variable with PowerShell:
			PS > $Env:LEARN_EMAIL = 'test@test.com' >> C:\\Users\rodri\\Documents\\WindowsPowerShell\\profile.ps1
			PS > $Env:LEARN_PASSWD = 'reallystrongpassword' >> C:\\Users\rodri\\Documents\\WindowsPowerShell\\profile.ps1
		
		Setting environment variable in Linux:
			For Bash users:
				$ echo "export LEARN_EMAIL='test@test.com' >> ~/.bashrc
				$ echo "export LEARN_PASSWD='reallystrongpasswd' >> ~/.bashrc

			For Zsh users:
				$ echo "export LEARN_EMAIL='test@test.com' >> ~/.zshrc
				$ echo "export LEARN_PASSWD='reallystrongpasswd' >> ~/.zshrc
		
		[Note]: the program expects variables names to be set as LEARN_EMAIL
		for learn dot email and LEARN_PASSWD for learn dot password
		"""
		return environ["LEARN_EMAIL"], environ["LEARN_PASSWD"]

	# Prompt for creds
	email = input("Enter LearnDot email: ")
	passwd = getpass("Enter LearnDot Password: ")
	return email, passwd


def arg_parse():
	from argparse import ArgumentParser
	parser = ArgumentParser(description="Automate the creation of office hours for Fullstack Academy")
	parser.add_argument("-e", "--email", help="LearnDot Email")
	parser.add_argument("-p", "--passwd", help="LearnDot Password")
	parser.add_argument("-v", "--env", action="store_true", help="use LEARN_EMAIL and LEARN_PASSWD environment variables for authentication")
	return parser.parse_args()

def main():
	# Parse programs arguments
	args = arg_parse()

	# Get operating system
	system_ = system()

	# Get users home directory
	user_home_dir = str(Path.home())

	# Office hours creation link
	url = "https://learn.fullstackacademy.com/officehours/form/add"

	# Get absolute path to chrome driver
	if system_ == "Windows":
		path_to_driver = user_home_dir + "\\Documents\\chromedriver.exe"
	else:
		path_to_driver = user_home_dir + "/Documents/chromedriver"

	if not args.email or not args.passwd:
		email, passwd = get_login(from_env=args.env)
		driver = open_learndot_tab(path_to_driver, url, email=email, passwd=passwd)
	else:
		driver = open_learndot_tab(path_to_driver, url, email=args.email, passwd=args.passwd)

	# Load JSON values from file into a Python Dictionary
	values = load(open("values.json", "r"))
	print("[%s* * *%s] Loading office hours options ..." % (fg(94), attr(0)))

	# Call function to create office hours
	create_office_hours(driver, url, values=values)

	# Close chrome driver
	driver.quit()

	print(
		"\n[%sREPORT%s %s %s] All office hours have been scheduled !!!"
		% (fg(129), attr(0), date.today().strftime("%m/%d/%y"), 
		datetime.now().strftime("%H:%M:%S"))
	)


if __name__ == "__main__":
		main()
