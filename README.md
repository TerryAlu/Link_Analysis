# Link Analysis - Hits, PageRank, SimRank

This project implemtns Hits, PageRank and SimRank algorithms.

## Environment

* OS: Ubuntu 16.04
* Pyhton version: 2.7.12

## Usage

###  Input Format

    # Each row represents a link from first to second
    1,2
    2,3
    ..
    ..
    
###  Command

`./experiments.sh` can output results for this homework to results.txt

Notice: Modify EPSILON variable in python files if you need

- hits.py
    - python hits.py \<infile path\>
- pagerank.py
    - python pagerank.py \<infile path\>
- simrank.py
    - python simrank.py \<infile path\>


## Tools

* fullmesh.py \<number of nodes\> \<output filepath\>
    * Create full mesh graph
* experiments.sh
    * Download datasets and output the result of the following experiments to results.txt
        * Experiment1: HITS & Pagerank - 6 graphs
        * Experiment2: HITS & Pagerank - transaction data from project 1
        * Experiment3: SimRank
        * Experiment4: Performance
* hw3dataset/download_dataset.sh
    * Download datasets used by experiments.sh from google drive
* gdrive_dl.sh \<google file id\> \<outfile name\>
    * Script for downloading file from google drive
