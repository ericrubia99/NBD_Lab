"""Utility classes and functions for reading data."""

from dataclasses import dataclass


@dataclass
class Packet:
    dscp_label: int
    header_len: int
    ds_field: int
    ds_field_ecn: int
    length: int
    protocol: int
    flag_df: int
    flag_mf: int
    flag_rb: int
    fragment_off: int
    ttl: int
    ip_src: str
    ip_dest: str
    port_src: str
    port_dest: str
    time: float


def decode_packet(packet):
    """Decodes a PcapReader packet.

    :arg
        packet (): the PcapReader packet.

    :return
        (Packet) the decoded packet.
    """
    network_type = packet.payload.name

    if network_type == 'IP':
        ip_version = packet.payload.fields['version']

        if ip_version == 6:
            return None

        time = float(packet.time)
        protocol = packet.payload.fields['proto']
        length = packet.payload.fields['len']
        flag = str(packet.payload.fields['flags'])
        flag_df = 1 if flag == 'DF' else 0
        flag_mf = 1 if flag == 'MF' else 0
        flag_rb = 1 if flag == 'RB' else 0
        fragment_offset = packet.payload.fields['frag']
        ip_src = packet.payload.fields['src']
        ip_dest = packet.payload.fields['dst']
        tos = f'{packet.payload.fields["tos"]:08b}'
        dscp_label = int(tos, 2)
        dscp = int(tos[:6], 2)
        ecn = int(tos[6:], 2)
        ttl = packet.payload.fields['ttl']

        transport_type = packet.payload.payload.name

        if transport_type == 'ICMP' or 'NoPayload':
            port_src = -1
            port_dest = -1
        else:
            port_src = packet.payload.payload.fields['sport']
            port_dest = packet.payload.payload.fields['dport']

        return Packet(dscp, 20, dscp_label, ecn, length, protocol, flag_df, flag_mf, flag_rb, fragment_offset, ttl,
                      ip_src, ip_dest, port_src, port_dest, time)
