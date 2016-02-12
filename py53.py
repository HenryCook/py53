#!/usr/bin/env python

import argparse

import sys

import boto3


client = boto3.client('route53')


def parse_args():
    parser = argparse.ArgumentParser(description='route53 management')
    parser.add_argument('-l', '--list_zones', action='store_true', help='Lists hosted zones')
    args = parser.parse_args()
    return args


def host_records():
    response = client.list_hosted_zones()
    print response


def main():
    args = parse_args()

    if args.list_zones:
        host_records()
    else:
        sys.exit()
    pass


if __name__ == '__main__':
    main()