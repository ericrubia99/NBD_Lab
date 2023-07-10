# Purpose
The purpose of this package is to provide functionality for Part A.2, *Time Evaluation between Sequential 
and Parallel reading* of the `.pcap` file.

# Read Script
The read script times the reading of a provided `.pcap` file in a sequential or parallel way, and saves the measure time.
When running the reading in parallel, you can also specify the number of parallel processes and the number of packets 
in each parallel process.

## How to run sequential read
```bash
python read.py -s -f=<path to pcap file> -o=<path to output directory> -v
```

Flags:

* `-s`: sequential processing.
* `-v`: verbose, will print out a tqdm loop.

## How to run parallel read
```bash
python read.py -p -f=<path to pcap file> -o=<path to output directory> -v -n=<number of packets per split> -m=<max number of parallel processes>
```

Flags:

* `p`: parallel processing.
* `-v`: verbose, will print out a tqdm loop.