"""Functions for reading parallell files."""
import glob
import os
import shutil
import time
from multiprocessing import Manager, Process

from tqdm import tqdm

from reading import read_sequential


def read_parallel(file_path: str, packets_per_file: int, max_parallel_processes: int, verbose=False):
    """Reads a pcap file in parallel and creates a dataframe of its contents.

    :arg
        file_path (str): path to the .pcap file to read.
        packets_per_file (int): the number of packets to put in each smaller .pcap file.
        max_parallel_processes (int): the maximum number of parallel processes to run.
    """

    # create directory where to put temporary pcap files
    sub_dir = "tmp/"

    # Remove directory if already exists
    if os.path.exists(sub_dir):
        shutil.rmtree(sub_dir)

    try:
        os.mkdir(sub_dir)
    # If you have already created it Error
    except OSError:
        print(f"Creation of the directory {sub_dir} failed")
    else:
        print(f"Successfully created the directory {sub_dir}")

    # split pcap file into different files, into the previous subdirectory
    os.system(f'editcap -c {packets_per_file} {file_path} {sub_dir}__mini.pcap')

    # find all created files
    files = sorted(glob.glob(f"{sub_dir}*.pcap"))

    # create subprocesses for reading files
    manager = Manager()

    start_time = time.time()

    processes = []

    for i, file in tqdm(enumerate(files), disable=not verbose):
        process = Process(target=read_sequential, args=(file,))

        processes.append(process)

        process.start()

        if i % max_parallel_processes == 0 and i > 0:
            print("Maximum number of process reached")
            for process in processes:
                process.join()

            print("All subprocesses finished")
            processes = []
