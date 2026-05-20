#!/bin/python3
"""
Backup of the seagate HD
"""
from pathlib import Path
import subprocess
from backup import sync_command, seagate_check

SEAGATE_BACKUP_UUID= '6eeeb7f8-1f9d-457e-8b0a-5969c123ea88' # Specify the UUID of your drive


# path base para o backup
origem_base = Path("/","home", "rouse")
destino_backup = Path("/","media", "seagate_backup")

# backup folders
documents = "Documents"
pictures = "Pictures"
videos = Path("Videos")

def is_mounted(mount_path):
    """Check if the given path is mounted."""
    return mount_path.is_mount()

def mount_drive(uuid, mount_path):
    """Mount the drive using its UUID if it's not already mounted."""
    
    subprocess.run(["sudo", "mkdir", "-p", str(mount_path)], check=True)
    subprocess.run(["sudo", "mount", f"UUID={SEAGATE_BACKUP_UUID}", mount_path], check=True)


def unmount_drive(mount_path):
    """Unmount the drive."""
    try:
        subprocess.run(["sudo", "umount", mount_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to unmount {mount_path}. It may not be mounted.")

# Attempt to unmount the drive first
unmount_drive(destino_backup)

# Check if Seagate is mounted
if not is_mounted(destino_backup):
    mount_drive(SEAGATE_BACKUP_UUID, destino_backup)

try:
    # Execute backup
    sync_command(origem_base, destino_backup, documents)
    sync_command(origem_base, destino_backup, pictures)
    sync_command(origem_base, destino_backup, videos)

finally:
    # Ensure the SSD is unmounted after the backup
    if is_mounted(destino_backup):
        unmount_drive(destino_backup)
        print('seagate_backup is umounted!')


