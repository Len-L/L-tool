
import time 
import subprocess

while True:
    print(" ")
    print(" ")
    print("1. scan port ")
    print("2. scan port 'full'")
    print("3. bruteforce login ssh")
    print("4. exit")
    print(" ")
    a = input("Choice-> ")
    print(" ")
    print(" ")

    if a=="1":
        b = input("ip-> ")
        subprocess.run(["nmap", b])

    if a=="2":
        b = input("ip-> ")
        subprocess.run(["nmap", "-A", b])

    if a=="3":
        b = input("ip-> ")
        c = input("password list-> ")
        d = input("username list-> ")
        print("add command = ssh://"+b)
        e = input("command -> ")
        subprocess.run(["hydra", "-L", d, "-P", c, "-t", "4", e])

    if a=="4":
        print("bye")
        break



