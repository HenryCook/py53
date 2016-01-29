#!/usr/bin/env python

import argparse
import boto3


client = boto3.client('route53')


def parse_args():
    parser = argparse.ArgumentParser(description='route53 management')
    parser.add_argument('-z', '--list_zones', action='store', help='Lists hosted zones')
    return parser


def host_records(list_zones):
    response = client.list_hosted_zones()
    return response


def main():

    parser = parse_args()
    args = parser.parse_args()

    host_records(args.list_zones)


if __name__ == '__main__':
    main()