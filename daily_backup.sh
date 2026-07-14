#!/bin/bash

SOURCE=$1
TODAY=$(date +%Y-%m-%d)
BACKUP_NAME="${SOURCE}_${TODAY}"

cp -r $SOURCE $BACKUP_NAME

echo "Backup complete: $BACKUP_NAME created."