#!/bin/bash

if [ ! $# -eq 2  ]
then
    echo "./gdrive_dl.sh <id> <outfile>"
    exit 1
fi

id="$1"
tmp="/tmp/cookies.txt"
outfile="$2"

wget --load-cookies ${tmp} "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ${tmp} --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id='${id} -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=${id}" -O ${outfile}
