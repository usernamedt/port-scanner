import argparse
import sys

from scanner import Scanner


def main():
    parser = argparse.ArgumentParser(
        description='Super fancy port checker.')

    parser.add_argument('host', type=str,
                        help='target IP or domain name')

    parser.add_argument('start', type=int,
                        help='port scan start port')

    parser.add_argument('end', type=int,
                        help='port scan end port')

    parser.add_argument('-t', type=float,
                        help='Option to specify tcp connection timeout (in seconds).',
                        required=False, default=1)

    args = parser.parse_args()

    if not 1 <= args.end <= 65535 or not 1 <= args.start <= 65535:
        print('Ports should be in range from 1 to 65535')
        sys.exit(-1)

    if args.start > args.end:
        print('Scan start should be smaller than end')
        sys.exit(-1)

    scanner = Scanner(args.t)
    scanner.scan_range(args.host, args.start, args.end)


if __name__ == "__main__":
    main()
