#usr/bin/python3 - 2020.08.29 - #Tayentu

import os
import requirements

print("""#İnstallation Program Script
        # 1-)  Yay package repo
        # 2-)  Vim Editor
        # 3-)  Metasploit
        # 4-)  Searchsploit 
        # 5-)  Nmap
        # 6-)  arp-scan
        # 7-)  Wireshark
        # 8-)  virtualbox
        # 9-)  Ulauncher
        # 10-) Jdownloader
        # 11-) Google-Chrome
        # 12-) VSCode
        # 13-) Wps Office
        # 14-) Telegram Desktop
        # Added will next days """)

def upgrade_repository():
    try:
        print("System Update and upgrade_repository.")
        os.system("sudo pacman -Syy")
    except:
        print("Error. Exiting")
    finally:
        print("Sucsessfulyy upgrade_repository. Next Step Pacman İnstall.")
def pacman_install(name):
    try:
        print(f"İnstall {name} package repo")
        os_install = "sudo pacman -S " + name + " --noconfirm"
        os.system(os_install)
        return True
    except:
        print(f"Error {name} install, Please read error code")
        return False
    finally:
        print("Sucsessfulyy upgrade_repository. Next Step Yay İnstall.")
 
        
def yay_install(name):
    try:
        print(f"İnstall {name} package repo")
        os_install = "yay -S "+name+" --nocleanmenu --nodiffmenu --noconfirm"
        os.system(os_install)
        return True
    except:
        print(f"Error {name} install, Please read error code")
        return False
    finally:
        print("Sucsessfulyy yay_install. Next Step Nvidia Driver İnstall.")

        
def nvidia_driver():
    try:
        print("İnstalling Nvidia-Driver")
        os.system("sudo mhwd -i pci video-modesetting")
        os.system("sudo mhwd -a pci nonfree 0300")
    except:
        print("Error install, Please read error code")

pacman = ["yay","vim","nmap","arp-scan","virtualbox","vscode","wpscan","telegram-desktop"]
yay = ["metasploit","exploit-db-git","wireshark","ulauncher","jdownloader2","google-chrome","wps-office"]

upgrade_repository()

for i in pacman:
    pacman_install(i)
    os.system("clear")
    
print("Sucsessfulyy pacman_install. Next Step yay_install.")

for i in yay:
    yay_install(i)
    os.system("clear")
print("Sucsessfulyy yay_install. Next Step Nvidia Driver İnstall.")

nvidia_driver()

