#!/bin/bash 

dataset_dir="hw3dataset/"
fullmesh_dir="${dataset_dir}fullmesh/"

fullmesh_exec="fullmesh.py"

## Generate fullmesh data from 2~2^12

if [ ! -d ${fullmesh_dir} ]; then
    mkdir ${fullmesh_dir}
fi

i=1
no=12

while [ $i -le $no ]
do
    n="$(echo 2^$i | bc)"
    echo -e "\t ${n}"

    filename="f_$n.txt"
    filepath="${fullmesh_dir}${filename}"

    python ${fullmesh_exec} ${n} ${filepath}

    ((i++))
done
