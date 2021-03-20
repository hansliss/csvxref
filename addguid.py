#!/usr/bin/env python3

"""addguid.py: Add a GUID column to a CSV file."""

__author__ = "Hans Liss"
__copyright__ = "Copyright 2021, Hans Liss"
__license__ = "BSD 2-Clause License"
__version__ = "1.0"
__maintainer__ = "Hans Liss"
__email__ = "Hans@Liss.nu"
__status__ = "Testing"

import csv
import uuid
import sys
import os
import datetime
import configparser
import argparse

## Read command-line parameters and configuration file
parser = argparse.ArgumentParser(description='Find changes in CardReaders')
parser.add_argument('-f', '--mainfile', required=True,
                    help='path to main CSV file')
parser.add_argument('-n', '--newcol', required=True,
                    help='new column to create in main file, with keys')
parser.add_argument('-d', '--dialect', required=True, default='excel',
                    help='new column to create in main file, with keys')

args = parser.parse_args()

with open(args.mainfile, newline='') as infile:
    os.rename(args.mainfile, args.mainfile + '~')
    with open(args.mainfile, 'w', newline='') as outfile:
        inreader = csv.DictReader(infile, delimiter=',', quotechar='"')
        headers = inreader.fieldnames
        headers.append(args.newcol)
        outwriter = csv.DictWriter(outfile, fieldnames=headers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect=args.dialect)
        outwriter.writeheader()
        for row in inreader:
            row[args.newcol] = str(uuid.uuid4())
            outwriter.writerow(row)

