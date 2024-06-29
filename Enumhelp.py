#!/bin/python3

Service_enum = input("What service are you enumerating? ")

Enumeration = {
	  'FTP': '\n[+] Did you run an NMAP scan \n[+] Did you scan all ports \n[+] Did you run it with -Pn flag\n[+] Are you damn sure you did not miss anything',
    'SSH': '\n[+] Version exploits \n[+] eneric credentials tried \n[+] Brute-force common User / password \n[+] Brute-force with known username and password list',
    'TELNET': '\n[+] Version exploits \n[+] Generic credentials tried \n[+] Brute-force common User / password \n[+] Brute-force with known username and password list',
    'SMTP': '\n[+] Version exploit \n[+] Brute force it',
    'DNS': '\n[+] Dig it? \n[+] Add new host and rescan?',
    'HTTP': '\n[+] Visually recon \n[+] Directory enumeration (manually & Auto) \n[+] Directory enumeration with extensions \n[+] Sub-Domain enumeration \n[+] Source code Search \n[+] OSINT search for users, Photos, address, ETC \n[+] Check for injectable field \n[+] Brute force logins (if applicable) \n[+] Bypass login attempted (if applicable) \n[+] Nikto \n[+] ZAP IT',
    'KERBEROS': '\n[+] Kerbute userenum & Bruteuser \n[+] Impacket tool kit \n[+] Roasted?',
    'RPC': '\n[+] Null login \n[+] Credentialed logon \n[+] Domain enumerated \n[+] Users enumerated \n[+] Domain enumerated \n[+] Attempted to add user',
    'SMB': '\n[+] enum4linux-ng \n[+] smbclient non credentialed & credentialed \n[+] crackmapexec',
    'LDAP': '\n[+] ldapsearch \n[+] Login bypass',
    'RDP': '\n[+] Spray Creds',
    'WINRM': '\n[+] Spray Creds'
}
for Z in Service_enum:
	for service, nudge in Enumeration.items():
		if service in Service_enum:
			print(f'For {service}:{nudge}')
			exit()
