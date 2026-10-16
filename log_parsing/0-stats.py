#!/usr/bin/python3
"""Read log lines and print accumulated metrics."""

import sys
import re


def print_stats(total_size, status_codes):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0

    pattern = (
        r'^(\S+) - \[.*?\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            match = re.match(pattern, line)

            if not match:
                continue

            code = int(match.group(2))
            size = int(match.group(3))

            if code not in valid_codes:
                continue

            total_size += size
            status_codes[code] = status_codes.get(code, 0) + 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
