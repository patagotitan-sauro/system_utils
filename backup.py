#!/bin/python3
"""
Program to syncronize backup in SanDisk hardware on /mnt/backup
I have to check if the drive is mounted
"""
from pathlib import Path
from datetime import datetime
from backup_lib import sync_command, seagate_check

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

