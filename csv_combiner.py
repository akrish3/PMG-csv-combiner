#!/usr/bin/env python3

import csv
import sys, getopt
import os.path as path

pathname = path.abspath(path.dirname(__file__))

def csv_combine(files, output='combined.csv'):
    """
    Purpose: Crates and opens new file. Loops of input files and 
    reads files line be line to limit memory usage. Appends data from 
    input files. Then writes new data to newly created file

    Input: 
        inputs - list of file names that will be read
        output - name of file that will be created and written too
    """
    with open(path.join(pathname,'', output), 'w', newline='') as file:
        if output == 'stdout':
            writer = csv.writer(sys.stdout)
        else:
             writer = csv.writer(file)
        for i, file_name in enumerate(files):
            parsedFileName = file_name.split('/')[-1]
            with open(path.join(pathname, '',file_name), newline='') as file:
                reader = csv.reader(file)
                for x, row in enumerate(reader):
                    if i > 0 and x == 0:
                        continue
                    if i == 0 and x == 0:
                        row.append('filename')
                        writer.writerow(row)
                        continue
                    row.append(parsedFileName)
                    writer.writerow(row)


def main(argv):
    opts, args = getopt.getopt(argv,"")
    files = args[1:len(args)-1]
    combined_output_type = args[-1]

    csv_combine(files, combined_output_type)
    

if __name__ == '__main__':
    main(sys.argv[0:])