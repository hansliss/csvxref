#!/usr/bin/env python3

"""csvxreg.py: Add secondary key references from a secondary CSV file to a new column in a CSV file."""

__author__ = "Hans Liss"
__copyright__ = "Copyright 2021, Hans Liss"
__license__ = "BSD 2-Clause License"
__version__ = "0.1"
__maintainer__ = "Hans Liss"
__email__ = "Hans@Liss.nu"
__status__ = "Testing"

import csv
import sys
import os
import datetime
import configparser
import argparse

## Read command-line parameters and configuration file
parser = argparse.ArgumentParser(description='Find changes in CardReaders')
parser.add_argument('-f', '--mainfile', required=True,
                    help='path to main CSV file')
parser.add_argument('-s', '--secfile', required=True,
                    help='path to secondary CSV file')
parser.add_argument('-l', '--logprefix',
                    help='prefix for log files. Datestamp will be added')
parser.add_argument('-v', '--valcol', required=True,
                    help='column in main file that contains the lookup value')
parser.add_argument('-L', '--lucol', required=True,
                    help='lookup column in secondary file, containing the lookup value')
parser.add_argument('-k', '--keycol', required=True,
                    help='key column in secondary file that contains the value to add to main file')
parser.add_argument('-n', '--newcol', required=True,
                    help='new column to create in main file, with keys')
parser.add_argument('-D', '--default', default=None,
                    help='default value to use when lookup value isn\'t found')
parser.add_argument('-d', '--dialect', required=True, default='excel',
                    help='new column to create in main file, with keys')

args = parser.parse_args()

if args.logprefix is not None:
    logfile = open(datetime.date.today().strftime(args.logprefix + "%Y-%m-%d"), "a")
    def log(str):
    	logfile.write(datetime.datetime.now().strftime("%H:%M:%S\t") + str + "\n")
else:
    def log(str):
        pass

with open(args.mainfile, newline='') as infile:
    os.rename(args.mainfile, args.mainfile + '~')
    with open(args.mainfile, 'w', newline='') as outfile:
        xlate = dict()
        with open(args.secfile, newline='') as secfile:
            secreader = csv.DictReader(secfile, delimiter=',', quotechar='"')
            for row in secreader:
                xlate[row[args.lucol]] = row[args.keycol]
            
        inreader = csv.DictReader(infile, delimiter=',', quotechar='"')
        headers = inreader.fieldnames
        headers.append(args.newcol)
        outwriter = csv.DictWriter(outfile, fieldnames=headers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect=args.dialect)
        outwriter.writeheader()
        for row in inreader:
            if (row[args.valcol] in xlate):
                row[args.newcol] = xlate[row[args.valcol]]
            else:
                if args.default:
                    row[args.newcol] = args.default
            outwriter.writerow(row)

