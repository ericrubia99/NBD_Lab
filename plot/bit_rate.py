"""Plotting function for bit rate."""

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
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


def plot_total_bit_rate(data: pd.DataFrame):
    bit_plot = px.line(data,
                       x=[i * 0.1 for i in range(1, len(list(map(lambda x: x/1e6, bit_rate(data, 0.1)))) + 1)],
                       y=list(map(lambda x: x/1e6, bit_rate(data, 0.1))),
                       template='plotly_white',
                       title='Total bit rate',
                       markers=True)
    bit_plot['data'][0]['showlegend'] = True
    bit_plot['data'][0]['name'] = '0.1 sec'
    bit_plot.add_scatter(x=[i * 0.4 for i in range(1, len(list(map(lambda x: x/1e6, bit_rate(data, 0.4)))) + 1)],
                         y=list(map(lambda x: x/1e6, bit_rate(data, 0.4))), name="0.4 sec")
    bit_plot.add_scatter(x=[i * 0.8 for i in range(1, len(list(map(lambda x: x/1e6, bit_rate(data, 0.8)))) + 1)],
                         y=list(map(lambda x: x/1e6, bit_rate(data, 0.8))), name="0.8 sec")
    bit_plot.update_layout(
        yaxis_title_text ='Mbps',
        xaxis_title_text ='Time(s)')

    bit_plot.show()
