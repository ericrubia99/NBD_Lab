import argparse
import os
import timeit
import logging
from pathlib import Path

import pandas as pd

from reading import read_parallel, read_sequential


if __name__ == '__main__':
    log_dir = "logs"
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    logging.basicConfig(format='%(name)s:%(levelname)s:%(asctime)s - %(message)s', handlers=[
        logging.FileHandler("debug.log", mode='a'),
        logging.StreamHandler()
    ])
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Reading files')

    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the pcap file to be read.")
    parser.add_argument('-o', '--out', type=str, required=True, help="Output directory where the timing data will be saved.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--parallel', action='store_true')
    group.add_argument('-s', '--sequential', action='store_true')
    args = parser.parse_args()

    if args.parallel:
        logger.info(f"Reading from {args.file} in parallel.")
        read_type = 'parallel'
        times = timeit.Timer(lambda: read_parallel(args.file, 1000, 100)).repeat(1, 1)
        logger.info(f"Finished reading.")

    elif args.sequential:
        logger.info(f"Reading from {args.file} sequentially.")
        read_type = 'sequential'
        times = timeit.Timer(lambda: read_sequential(args.file)).repeat(1, 1)

        logger.info(f"Finished reading.")

    if not os.path.exists(args.out):
        os.mkdir(args.out)

    out_path = f'{args.out}timing_{read_type}_{args.file.split("/")[-1].split(".")[0]}.feather'

    timing_df = pd.DataFrame([[read_type, min(times)]], columns=['read_type', 'time_s'])

    #if os.path.exists(out_path):
    #    logger.info(f"Found existing dataframe at {out_path}.")
    #    df = pd.read_feather(out_path)

    #    logger.info(f"Appending to existing dataframe.")
    #    timing_df = pd.concat((timing_df, df), axis=0, ignore_index=True)

    timing_df.to_feather(out_path)
    logger.info(f"Saved dataframe to {out_path}.")
