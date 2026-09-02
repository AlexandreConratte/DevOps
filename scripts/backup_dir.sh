#!/usr/bin/env bash
 echo "backup script started"


 if [ "$#" -ne 2 ]; then    #-ne not equal , verifie qu'il y ait bien 2 arguments
    echo "Usage: bash scripts/backup_dir.sh <source_dir> <dest_dir>"
    exit 2
  fi

 SOURCE_DIR="$1"
  DEST_DIR="$2"
  LOG_DIR="logs"
  LOG_FILE="$LOG_DIR/backup.log"

  mkdir -p "$LOG_DIR"    

#verifier que la source est bien un dossier sinon exit 2
   if [ ! -d "$SOURCE_DIR" ]; then
    MESSAGE="CRITICAL source_dir_not_found path=$SOURCE_DIR"
    echo "$MESSAGE"
    echo "$(date -Iseconds) $MESSAGE" >> "$LOG_FILE"
    exit 2
  fi

   mkdir -p "$DEST_DIR"  

   TIMESTAMP="$(date +%Y%m%d-%H%M%S)"    
  ARCHIVE_PATH="$DEST_DIR/backup-$TIMESTAMP.tar.gz" 

  #tar -czf "$ARCHIVE_PATH" "$SOURCE_DIR"   create, z = gzip, f = ecrire dans le fichier 

   if ! tar -czf "$ARCHIVE_PATH" "$SOURCE_DIR"; then    #si tar echoue 
     MESSAGE="CRITICAL backup_failed source=$SOURCE_DIR archive=$ARCHIVE_PATH"
  echo "$MESSAGE"
  echo "$(date -Iseconds) $MESSAGE" >> "$LOG_FILE"
  exit 2
fi

  MESSAGE="OK backup_created source=$SOURCE_DIR archive=$ARCHIVE_PATH"
  echo "$MESSAGE"
  echo "$(date -Iseconds) $MESSAGE" >> "$LOG_FILE"
  exit 0