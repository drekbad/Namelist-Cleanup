#!/usr/bin/python3

import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Process a list of names.')
parser.add_argument('-i', '--input', required=True, help='Input filename containing the list of names.')
parser.add_argument('-o', '--output', help='Output filename for the formatted list of names.')

args = parser.parse_args()

output_filename = args.output if args.output else f"formatted_names_list_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

with open(args.input, 'r') as infile, open(output_filename, 'w') as outfile:
    for name in infile:
        parts = name.strip().split('-')
        formatted_name = f"{parts[0].title()} {parts[-1].title()}\n"
        outfile.write(formatted_name)

print(f"Processed names are written in '{output_filename}'")
