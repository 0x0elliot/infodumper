# infodumper
InfoDumper is a python script which you can use in physical penetration testing of linux systems to steal Wi-Fi passwords, System user password hashes with clear text user names, IP Address of the system (Both local and global) and many more coming soon.

<h1>Features:</h1>

1. Obtain the clear text saved Wi-Fi passwords<br>
2. Obtain the local and Global IP Addresses of the system (Along with ifconfig data)<br>
3. Obtain the Hostname used by the system<br>
4. Get the users on that system and their hashed passwords from /etc/passwd and /etc/shadow<br>
<b>5. Have the output saved automatically into your pendrive so that you don't have to mess around much. </b>

<h1>Requirements:</h2>
1. You should already have root/sudoer access to the system.<br>
2. It should have Python installed in it.<br>
3. You need a pendrive/Hardrive.<br>
4. The system being pentested must be a linux system.

<h1>Usage:</h1>

First, Git clone this repository to your pendrive.

```
cd {path to your pendrive} #Or just move it after git cloning it to your desktop
git clone https://github.com/kiddocoder/infodumper
```



Next, Once your physical pentesting begins, Run the script and it will automatically fetch the data it needs into your pendrive under a couple seconds saving you some time.



```
sudo python3 {path_to_script}/infodumper.py
```

You will be asked two questions:

1. Which user are you logged in as (Name of the user account)<br>
2. What is the name of your pendrive (You will be shown the drives connected to your device. You just need to select yours.)<br>

<b>Coming soon:</b> InfoDumping Remotely to another server/computer you have access to, Without needing any physical access.
