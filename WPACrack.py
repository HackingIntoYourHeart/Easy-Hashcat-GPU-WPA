import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

hsFile = input("Path to handshake (.cap): ")
wordlist = input("Path to wordlist (.txt): ")
if wordlist == "":
	wordlist = "rockyou.txt"
	print("Defaulting to \"rockyou.txt\"...")

hccapxFile = ("".join(hsFile.split(".")[:-1])) + ".hccapx"
if not os.path.exists(hccapxFile):
	os.system("cap2hccapx " + hsFile + " " + hccapxFile)

"""

   2500 | WPA-EAPOL-PBKDF2                                 | Network Protocols
   2501 | WPA-EAPOL-PMK                                    | Network Protocols
  22000 | WPA-PBKDF2-PMKID+EAPOL                           | Network Protocols
  22001 | WPA-PMK-PMKID+EAPOL                              | Network Protocols
  16800 | WPA-PMKID-PBKDF2                                 | Network Protocols
  16801 | WPA-PMKID-PMK                                    | Network Protocols
  
"""

os.system("hashcat -w 3 -D 2 -o " + ("".join(hsFile.split(".")[:-1])) + "_creds.txt -a 0 -m 2500 " + hccapxFile + " " + wordlist)

if os.path.exists( ("".join(hsFile.split(".")[:-1])) + "_creds.txt" ):
	print("\nCreds:")
	with open( (("".join(hsFile.split(".")[:-1])) + "_creds.txt"), 'r') as cracked:
		print(cracked.read())

print("\nDone")
input()
