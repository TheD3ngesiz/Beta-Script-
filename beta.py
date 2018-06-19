#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os as th3
import sys
th3.system('clear' if th3.name == 'nt' else 'reset')

print("""

 [1] Change Password 
 [2] Add User 
 [3] Change Hostname 
 [4] About

	""")
sa = raw_input("Which of the above ? : ")
if sa == "1":
	cmd1 = raw_input("Username : ")
	cmd2 = th3.system("sudo passwd " + cmd1)
	th3.system('clear' if th3.name == 'nt' else 'reset')
	print("Changed Successfully ✔")
	quit()

if sa == "2":
	cmd3 = raw_input("Username: ")
	cmd4 = th3.system("sudo adduser " + cmd3)
	th3.system('clear' if th3.name == 'nt' else 'reset')
	print("Insert Successfully ✔")
	quit()

if sa == "3":
	cmd6 = raw_input("There will be a few transactions in the back. Do you allow ? Y/h: ")
	if cmd6 == "Y":
		cmd5 = raw_input("HostName: ")
		cmd7 = th3.system("touch hostname")
		cmd8 = th3.system("echo " + cmd5 + ">>hostname")
		cmd9 = th3.system("rm -r /etc/hostname")
		cmd0 = th3.system("cp hostname /etc/")
		cmd10 = th3.system("rm -r hostname")
		th3.system('clear' if th3.name == 'nt' else 'reset')
		reboot = raw_input("Restart the machine ? Y/n:")
		if reboot == "Y":
			cmd12 = th3.system("reboot")

		else:
			print("Permission required !")
			quit()

	else:
		print("Permission required !")
		quit()


if sa == "4":
	print("""

		@rootTheDengesiz >> Twitter account
		https://turkdefarmy.com/ >> TheDengesiz
		https://www.youtube.com/channel/UC5aJBYTWqCrZbfMVCTmCVbw >> YouTube 

		Wait for me !

		""")


