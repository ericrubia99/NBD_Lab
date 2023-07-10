"""Script for comining timing results dataframes into a single dataframe."""
import glob
from pathlib import Path
import logging
import argparse
from functools import reduce
import pandas as pd

if __name__ == '__main__':
    log_dir = "logs"
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    logging.basicConfig(format='%(name)s:%(levelname)s:%(asctime)s - %(message)s', handlers=[
        logging.FileHandler("debug.log", mode='a'),
        logging.StreamHandler()
    ])
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Combining files')

    parser.add_argument('-p', '--path', type=str, required=True, help="Path to the directory of result feather dataframes.")
    parser.add_argument('-o', '--out', type=str, required=True,
                        help="Output directory where the combined timing data will be saved.")

    args = parser.parse_args()

    logger.info(f"Reading files from {args.path}")
    timing_df = reduce(lambda a, b: pd.concat((a, b), axis=0, ignore_index=True),
                       map(lambda df_path: pd.read_feather(df_path), glob.glob(f"{args.path}*.feather")))

    parallel_times = timing_df[timing_df.read_type == 'parallel']
    sequential_times = timing_df[timing_df.read_type == 'sequential']

    out_path = f"{args.out}reading_times.feather"
    logger.info(f"Saving combined dataframe to {out_path}")
    timing_df.to_feather(out_path)
