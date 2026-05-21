#!/bin/bash

echo "Backup to OneDrive started at: $(date +"%Y-%m-%d %H:%M:%S")"

#!/bin/bash

/usr/bin/rclone sync $HOME/Documents OneDrive:Linux_Documents \
    --log-file=$HOME/rclone-backup.log \
    --log-level INFO \
    -v

echo "***"
echo "Fase 3: Sincronização para a nuvem feita."
echo "***"
