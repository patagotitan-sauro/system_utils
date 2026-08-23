# system_utils

A collection of small, standalone Linux scripts for managing a personal machine: backups, system monitoring, and one-off setup tasks. Each script is self-contained and run directly — there's no shared build system or install step beyond the Python dependencies noted below.

## Backups

### `backup.py`
Rsyncs `~/Documents`, `~/Pictures`, and `~/Videos` to a locally mounted drive at `/mnt/backup` (e.g. a SanDisk drive), using `rsync -rva --delete`.

```
./backup.py
```

### `seagate_backup.py`
Same backup targets, but to a Seagate SSD. Mounts the drive by UUID before backing up and unmounts it afterward (via `sudo`), so requires sudo privileges.

```
./seagate_backup.py
```

Edit `SEAGATE_BACKUP_UUID` in the script to match your drive.

### `backup_lib.py`
Shared library used by both `backup.py` and `seagate_backup.py` — not run directly. Holds `sync_command()` (the rsync wrapper) and `seagate_check()`.

### `rclone_onedriveBackup.sh`
One-way sync of `~/Documents` and `~/Pictures` to OneDrive via `rclone sync` (mirrors local → remote, deleting remote files no longer present locally). Logs to `~/rclone-backup.log`.

Requires an `rclone` remote named `OneDrive` already configured (`rclone config`).

```
./rclone_onedriveBackup.sh
```

## Monitoring

### `monitor.py`
Polls CPU and RAM usage every 10 seconds (and GPU/VRAM usage if `GPUtil` is installed), appending each sample to `system_metrics.csv` in the current directory. Runs until stopped with Ctrl+C.

```
pip install -r requirements.txt  # GPUtil is optional
./monitor.py
```

## Utilities

### `rename.sh`
Batch-renames `Whats*.jpeg` and `IMG*.JPG` files in the current directory to `<base_name>_foto_<n>.<ext>`. Prompts interactively for the base name.

```
./rename.sh
```

### `ubuntuSetup.sh`
One-off setup routines for Ubuntu/Zorin, dispatched by function name:

```
./ubuntuSetup.sh install_flatpak   # installs Flatpak + adds Flathub remote
./ubuntuSetup.sh install_sober     # installs Sober via Flatpak
./ubuntuSetup.sh install_kvm       # installs KVM/QEMU + virt-manager
```

## Requirements

- Python 3
- `rsync`, `rclone` (for the respective backup scripts)
- Python packages in `requirements.txt` (`psutil`; `GPUtil` is optional, only needed for GPU/VRAM stats in `monitor.py`)

## License

CC0 1.0 Universal — see [LICENSE](LICENSE).
