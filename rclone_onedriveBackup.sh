#!/bin/bash

#echo "Backup to OneDrive started at: $(date +"%Y-%m-%d %H:%M:%S")"

/usr/bin/rclone sync $HOME/Documents OneDrive:Linux_Documents \
    --log-file=$HOME/rclone-backup.log \
    --log-level INFO \

#Atenção revisar o folder do Onedrive antes de por o script em produção!!!!
/usr/bin/rclone sync $HOME/Pictures OneDrive:Linux_Pictures \
    --log-file=$HOME/rclone-backup.log \
    --log-level INFO \
#echo "***"
#echo "Sincronização para a nuvem feita."
#echo "***"
