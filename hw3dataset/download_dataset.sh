#!/bin/bash

## download

download_script="./gdrive_dl.sh"

project3dataset_filename="project3dataset.zip"
if [ ! -f ${project3dataset_filename} ]; then
    # download
    project3dataset_id="16o8BeSL2f2uAjdz9q1qjqBZii6H_UMHi"
    ${download_script} ${project3dataset_id} ${project3dataset_filename}

    # unzip & move data to current folder
    unzip ${project3dataset_filename}
    mv ./hw3dataset/* .
    rm -rf ./__MACOSX
    rm -rf ./hw3dataset
fi

ibm_dataset_filename="test_10000.data"
if [ ! -f ${ibm_dataset_filename} ]; then
    ibm_dataset_id="1nQcFE0h0kIbdxvXhR6DNK5MbRL8Zzb0F"
    ${download_script} ${ibm_dataset_id} ${ibm_dataset_filename}
fi
