"""Module for reading pcap data sequentially."""

import pandas as pd
from scapy.utils import PcapReader

from .util import decode_packet


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
