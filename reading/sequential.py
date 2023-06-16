"""Module for reading pcap data sequentially."""

import pandas as pd
from scapy.all import *

from .util import decode_packet
from tqdm import tqdm


def read_sequential(file_name: str):
    """Reads the pcap file at the given location and creates a pandas dataframe with the packets in the file.

    :arg
        file_name (str): the path to the pcap file.

    :return
        (pd.DataFrame) a dataframe with the decoded packets.
    """
    packets = []

    for pkt in PcapReader(file_name):

        packet = decode_packet(pkt)
        if packet:
            packets.append(packet)

    return pd.DataFrame([vars(p) for p in packets])



if __name__ == '__main__':

    df = read_sequential("../data/packets.pcap")
    df.to_feather('alt_packets.feather')