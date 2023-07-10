"""Module for plotting function for reading timing results."""

import pandas as pd
import matplotlib.pyplot as plt

def plot_read_time(sequential_times: pd.DataFrame, parallel_times: pd.DataFrame):
    """Creates a figure of the read time data."""

    fig, ax = plt.subplots()
    n = parallel_times.shape[0]
    ax.plot(parallel_times.n_packets, parallel_times.time_s, label="Parallel")
    ax.plot(sequential_times.n_packets, sequential_times.time_s, label="Sequential")
    ax.set_xticks([10 ** i for i in range(1, n + 1)], [f"$10^{i}$" for i in range(1, n + 1)])
    ax.legend()
    ax.set_xscale("log")
    ax.set_xlabel("Number of Packets")
    ax.set_ylabel("Seconds")
    ax.set_title("Sequential vs Parallel Processing of pcap Files")

    return fig, ax
