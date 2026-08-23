# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A small collection of independent, standalone Linux system-administration scripts for a single personal machine (user `rouse`, hostname paths under `/home/rouse`). There is no shared build system, package manager, test suite, or CI — each script is self-contained and run directly (`./script.sh` or `python3 script.py`). Changes to one script generally have no effect on the others, except where noted below.

## Scripts

- **backup_lib.py** — Shared library holding `sync_command()` (rsync a folder with `--delete`) and `seagate_check()`. Imported by both `backup.py` and `seagate_backup.py`; edits here affect both scripts.
- **backup.py** — Rsyncs `~/Documents`, `~/Pictures`, and `~/Videos` to a locally mounted drive at `/mnt/backup`, using `sync_command()` from `backup_lib.py`.
- **seagate_backup.py** — Backs up the same folders to a Seagate SSD, mounted/unmounted by UUID (`SEAGATE_BACKUP_UUID`) via `sudo mount`/`sudo umount`. Uses `sync_command`/`seagate_check` from `backup_lib.py`.
- **rclone_onedriveBackup.sh** — Syncs `~/Documents` and `~/Pictures` to OneDrive via `rclone sync` (one-way, mirrors local → remote, deletes remote files not present locally). Logs to `~/rclone-backup.log`. Assumes an `rclone` remote named `OneDrive` is already configured.
- **monitor.py** — Polls CPU/RAM (via `psutil`) and, if `GPUtil` is installed, VRAM/GPU usage every `SAMPLE_INTERVAL` (10s) and appends rows to `system_metrics.csv` in the working directory. Runs until Ctrl+C.
- **rename.sh** — Interactively batch-renames `Whats*.jpeg` and `IMG*.JPG` files in the current directory to `<base_name>_foto_<n>.<ext>`, prompting for the base name.
- **ubuntuSetup.sh** — A dispatcher script for one-off machine setup on Ubuntu/Zorin: run as `./ubuntuSetup.sh <function_name>` (e.g. `./ubuntuSetup.sh install_flatpak`, `install_sober`, `install_kvm`). The first CLI argument is invoked directly as a shell function name, so any new setup routine added to this file should follow the same `install_*` naming and be called the same way.

## Conventions specific to this repo

- The two Python backup scripts (`backup.py`, `seagate_backup.py`) share logic via `backup_lib.py` — edit `sync_command()`/`seagate_check()` there, not in either script.
- Destination paths and drive identifiers (mount points, UUIDs, rclone remote names) are hardcoded for this specific machine, not read from config/env files. When editing these scripts, preserve that pattern unless asked to generalize it.
- Backup scripts use `rsync -rva --delete` / `rclone sync` (mirror mode) — destination files not present at the source are deleted. Be careful when changing source/destination arguments.
- Scripts that touch mounted drives or `sudo mount`/`umount` assume passwordless or already-authenticated `sudo`.
