[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)]
<br>
![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/) 
![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

# infodumper
InfoDumper is a python script which you can use in physical penetration testing of linux systems to steal Wi-Fi passwords, System user password hashes with clear text user names, IP Address of the system (Both local and global) and many more coming soon.

<h1>Features:</h1>

1. Obtain the clear text saved Wi-Fi passwords<br>
2. Obtain the local and Global IP Addresses of the system (Along with ifconfig data)<br>
3. Obtain the Hostname used by the system<br>
4. Get the users on that system and their hashed passwords from /etc/passwd and /etc/shadow<br>
5. <b>Have the output saved automatically into your pendrive so that you don't have to mess around much. </b>

<h1>Requirements:</h2>
1. You should already have root/sudoer access to the system.<br>
2. It should have Python installed in it.<br>
3. You need a pendrive/Hardrive.<br>
4. The system being pentested must be a linux system.

<h1>Usage:</h1>

First, Git clone this repository to your pendrive.

```
cd {path to your pendrive} #Or just move it after git cloning it to your desktop
git clone https://github.com/0x0elliot/infodumper
```



Next, Once your physical pentesting begins, Run the script and it will automatically fetch the data it needs into your pendrive under a couple seconds saving you some time.



```
sudo python3 {path_to_script}/infodumper.py
```

You will be asked two questions:

1. Which user are you logged in as (Name of the user account)<br>
2. What is the name of your pendrive (You will be shown the drives connected to your device. You just need to select yours.)<br>

<h1>Who is InfoDumper for?</h1>
Pentesters who have to physically pentest systems and networks. I have tried my best to make their job a little faster and a little more easier <3
<br>
<h1>Bugs Fixed:</h1>
1. Has a better looking name for the txt files.<br>
2. Fixed the FileNotFound error it showed :/ pretty silly ikr

<br>
<br>


<b>Coming soon:</b> InfoDumping Remotely to another server/computer you have access to, Without needing any physical access.
