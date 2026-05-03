#!/bin/python3
"""
Program to syncronize backup in SanDisk hardware on /mnt/backup
I have to check if the drive is mounted 
"""
import os
from pathlib import Path
from datetime import datetime

def sync_command(origem, destino, folder):
    origem = origem / folder
    destino = destino
    if os.path.exists(origem) & os.path.exists(destino):
        print(f"""******* Backup of '{folder}' ******: \n
        -> origem: {origem}
        -> destino: {destino} \n""")
        os.system(f"rsync -rva --delete {origem} {destino}") 
        print(f"backup complete: {folder} \n*********x**********\n\n")
    else:
        print(f"Error with backup of:'{folder}'. Path is not valid.")

def seagate_check():
    if os.system("df -h | grep -h seagate_backup") == 0:
        print("ok, lets backup")
    else:
           if os.system("sudo mount /media/rouse/seagate_backup") == 0:
               print("Montei 'seagate_backup' drive.\n Lets backup now.")
           else:
               print("""Error: can't find /media/rouse/seagate_backup.
               Please, connect seagate ssd drive. """)
               exit()
    return None



if __name__ == "__main__":

    # path base para o backup
    origem_base = Path("/","home", "rouse")
    destino_backup = Path("/","mnt", "backup")

    # backup folders
    documents = "Documents"
    pictures = "Pictures"
    videos = Path("Videos")

    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

    sync_command(origem_base, destino_backup, documents)
    sync_command(origem_base, destino_backup, pictures)
    sync_command(origem_base, destino_backup, videos)

    print("Sucess in the Backup")

