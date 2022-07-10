
import os 
import time

while True:
    print("1. install tools with apt")
    print("2. install tools with pacman")
    print("3. exit")

    a = input("choice-> ")

    if a=="1":
        os.system("apt update")
        time.sleep(2)
        os.system("apt install nmap")
        time.sleep(2)
        os.system("apt install hydra")

    if a=="2":
        os.system("pacman -Sy")
        time.sleep(2)
        os.system("pacman -S nmap")
        time.sleep(2)
        os.system("pacman -S hydra")
        

    if a=="3":
        print("bye")
        break










