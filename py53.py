#!/usr/bin/env python

import argparse
import boto3
import sys


client = boto3.client('route53')


def parse_args():
    parser = argparse.ArgumentParser(description='route53 management')
    parser.add_argument('-z', '--list_zones', action='store_true', help='Lists hosted zones')
    args = parser.parse_args()
    return args


def host_records(args, list_zones):
    return client.list_hosted_zones_by_name(args.list_zones)


def main():
    args = parse_args()

    if args.list_zones is None:
        host_records(args.list_zones)
    else:
        sys.exit()
    pass


if __name__ == '__main__':
    main()