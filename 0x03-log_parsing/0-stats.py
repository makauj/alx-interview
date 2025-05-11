#!/usr/bin/python3
"""
Python script that reads lines from standard input,
processes them based on the specified format, and prints the required
statistics every 10 lines or when interrupted by CTRL + C
"""

import sys


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
    '500': 0
    }

totalSize = 0
count = 0

try:
    for _ in sys.stdin:
        line = _.split(" ")

        if len(line) > 4:
            status = line[-2]
            size = int(line[-1])
            totalSize += size
            count += 1

            if status in status_codes.keys():
                status_codes[status] += 1
        if count == 10:
            count = 0
            print("File size: {}".format(totalSize))

            for key in sorted(status_codes.keys()):
                if status_codes[key] != 0:
                    print("{}: {}".format(key, status_codes[key]))
except Exception as e:
    pass

finally:
    print(f"File size: {totalSize}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))
