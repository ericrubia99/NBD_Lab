"""Plotting function for bit rate."""

import matplotlib.pyplot as plt
import pandas as pd

from util import bit_rate


def plot_bit_rate(top_ip_data: pd.DataFrame, ip_data: pd.DataFrame, ip: str):
    row_length = int(top_ip_data.shape[0] / 2)

    fig, axs = plt.subplots(figsize=(20, 12),
                                    nrows=2, ncols=row_length,
                                    gridspec_kw=dict(hspace=0.4))

    for ip, ax in zip(top_ip_data.IP_DST, axs.flatten()):
        max_ip_data = ip_data[ip_data.IP_DST == ip]
        ax.plot(bit_rate(max_ip_data), marker="o")
        ax.set_title(ip)
        ax.set_xlabel("T (sec)")
        ax.set_ylabel("bit/sec")
    
    n = top_ip_data.shape[0]
    fig.suptitle(f'TOP {n} IP Dst for {ip}', fontsize=16)
    fig.show()