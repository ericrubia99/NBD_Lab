import argparse

from reading import read_parallel, read_sequential


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reading files')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--parallel', action='store_true')
    group.add_argument('-s', '--sequential', action='store_true')
    args = parser.parse_args()

    if args.parallel:
        read_parallel('data/packets.pcap', 1000, 100)
    elif args.sequential:
        read_sequential('data/packets.pcap')
