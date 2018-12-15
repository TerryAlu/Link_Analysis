#!/bin/bash 

dir="data/"
result_file="results.txt"
apriori_output="apriori.output"
fpg_output="fpg.output"

hits_exec="hits.py"
simrank_exec="simrank.py"
pagerank_exec="pagerank.py"


dataset_dir="hw3dataset/"
fullmesh_dir="${dataset_dir}fullmesh/"
ibm_data_dir="${dataset_dir}ibm_convert/"

# clear old experiment
echo "" > $result_file

## Experiment1: HITS & PageRank - 6 graphs
echo -e "\t\t Experiment1: HITS & Pagerank - 6 graphs" | tee -a ${result_file}

i=1
no=6

while [ $i -le $no ]
do
    filename="graph_${i}.txt"
    filepath="${dataset_dir}${filename}"

    echo -e "\n=== ${hits_exec}: ${filename} === \n" | tee -a $result_file
    python ${hits_exec} ${filepath} >> $result_file
    echo -e "\n=== ${pagerank_exec}: ${filename} === \n" | tee -a $result_file
    python ${pagerank_exec} ${filepath} >> $result_file

    ((i++))
done

echo "Done"

## Experiment2: HITS & PageRank - transaction data from project 1
echo -e "\t\t Experiment2: HITS & Pagerank - transaction data from project 1" | tee -a ${result_file}

filename="test_10000.data"
filepath="${ibm_data_dir}${filename}"

echo -e "\n=== ${hits_exec}: ${filename} === \n" | tee -a $result_file
python ${hits_exec} ${filepath} >> $result_file
echo -e "\n=== ${pagerank_exec}: ${filename} === \n" | tee -a $result_file
python ${pagerank_exec} ${filepath} >> $result_file

echo "Done"

## Experiment3: SimRank
echo -e "\t\t Experiment3: SimRank" | tee -a ${result_file}

i=1
no=5

while [ $i -le $no ]
do
    filename="graph_${i}.txt"
    filepath="${dataset_dir}${filename}"

    echo -e "\n=== ${simrank_exec}: ${filename} === \n" | tee -a $result_file
    python ${simrank_exec} ${filepath} >> $result_file

    ((i++))
done

echo "Done"

## Experiment4: Performance
echo -e "\t\t Experiment4: Performance" | tee -a ${result_file}

if [ ! -d ${fullmesh_dir} ]; then
    ./fullmesh.sh
fi

i=1
no=12

while [ $i -le $no ]
do
    n="$(echo 2^$i | bc)"

    filename="f_$n.txt"
    filepath="${fullmesh_dir}${filename}"

    echo -e "\n=== ${hits_exec}: ${filename} === \n" | tee -a $result_file
    (time python ${hits_exec} ${filepath} > /dev/null) 2>> $result_file
    echo -e "\n=== ${pagerank_exec}: ${filename} === \n" | tee -a $result_file
    (time python ${pagerank_exec} ${filepath} > /dev/null) 2>> $result_file

    ((i++))
done

echo "Done"

