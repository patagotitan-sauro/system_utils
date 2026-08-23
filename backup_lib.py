#!/bin/python3
"""
Shared helpers for backup.py and seagate_backup.py
"""
import os
import subprocess

def sync_command(origem, destino, folder):
    origem = origem / folder
    destino = destino
    if os.path.exists(origem) & os.path.exists(destino):
        print(f"""******* Backup of '{folder}' ******: \n
        -> origem: {origem}
        -> destino: {destino} \n""")
        subprocess.run(["rsync", "-rva", "--delete", str(origem), str(destino)])
        print(f"backup complete: {folder} \n*********x**********\n\n")
    else:
        print(f"Error with backup of:'{folder}'. Path is not valid.")

def seagate_check():
    result = subprocess.run("df -h | grep -h seagate_backup", shell=True)
    if result.returncode == 0:
        print("ok, lets backup")
    else:
           mount_result = subprocess.run(["sudo", "mount", "/media/rouse/seagate_backup"])
           if mount_result.returncode == 0:
               print("Montei 'seagate_backup' drive.\n Lets backup now.")
           else:
               print("""Error: can't find /media/rouse/seagate_backup.
               Please, connect seagate ssd drive. """)
               exit()
    return None
