import os
os.system('clear')
print('''\033[1;32m
                                @NAYZK17
                         
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
''')
print('''\033[1;32m
██████╗░░█████╗░██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝███████║██████╔╝░░░██║░░░
██╔═══╝░██╔══██║██╔══██╗░░░██║░░░
██║░░░░░██║░░██║██║░░██║░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
''')

print("\033[1;32m-"*64)         
print('')    
print('''\033[1;36m
[ 1 ] ===> install pkg [ Termux ]

[ 2 ] ===> install metasploit
''')
us = int(input('\033[1;32mEnter => '))
if us == 1:
	os.system('clear')
	print('''\033[1;33m
	────────────█████████
──────────███║║║║║║║███
─────────█║║║║║║║║║║║║║█
────────█║║║║███████║║║║█
───────█║║║║██─────██║║║║█
──────█║║║║██───────██║║║║█
─────█║║║║██─────────██║║║║█
─────█║║║██───────────██║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
────███████───────────███████
───██║║║║║║██────────██║║║║║██
──██║║║║║║║║██──────██║║║║║║║██
─██║║║║║║║║║║██───██║║║║║║║║║║██
██║║║║║║║║║║║║█████║║║║║║║║║║║║██
█║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█
█║║║║║║║║║║║║║█████║║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
██║║║║║║║║║║║█░░░░░█║║║║║║║║║║║██
██║║║║║║║║║║║║█░░░█║║║║║║║║║║║║██
─██║║║║║║║║║║║█░░░█║║║║║║║║║║║██
──██║║║║║║║║║║█░░░█║║║║║║║║║║██
───██║║║║║║║║║█░░░█║║║║║║║║║██
────██║║║║║║║║█████║║║║║║║║██
─────██║║║║║║║║███║║║║║║║║██
──────██║║║║║║║║║║║║║║║║║██
───────██║║║║║║║║║║║║║║║██
────────██║║║║║║║║║║║║║██
─────────██║║║║║║║║║║║██
──────────██║║║║║║║║║██
───────────██║║║║║║║██
────────────██║║║║║██
─────────────██║║║██
──────────────██║██
───────────────███
───────────────────────▄██▄▄██▄
──────────────────────██████████
──────────────────────▀████████▀
────────────────────────▀████▀
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
──────────────────────▄▄▄████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▄█████▀

	
	''')
	print('\033[1;33m                plase wait        ')
	os.system('termux-setup-storage;cd;dpkg --configure -a;pkg update -y;pkg upgrade -y;pkg install python -y;pkg install python2 -y;pkg install python2-dev -y;pkg install python3 -y;pkg install pip -y;pkg install pip2;pip2 install requests;pkg install fish -y;pkg install ruby -y;pkg install git -y;pkg install dnsutils -y;pkg install php -y;pkg install perl -y;pkg install nmap -y;pkg install bash -y;pkg install clang -y;pkg install nano -y;pkg install w3m -y;pkg install figlet -y;pkg install cowsay -y;gem install lolcat;pkg install curl -y;pkg install tar -y;pkg install zip -y;pkg install unzip -y;pkg install tor -y;pkg install wget -y;pkg install wgetrc -y;pkg install wcalc -y;pkg install bmon -y;pkg install unrar -y;pkg install toilet -y;pkg install proot -y;pkg install golang -y;pkg install chroot -y;termux-chroot -y;pkg install openssl -y;pkg install cmatrix -y;pkg install openssh -y;apt update && apt upgrade -y')
	os.system('python3 install.py')
else:
	if us == 2:
		os.system('clear')
		os.system('pkg install wget')
		os.system('wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh')
		os.system('chmod +x metasploit.sh')
		os.system('./metasploit.sh')






