#!/usr/bin/python3
"""Parse log lines and print accumulated metrics."""

import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read input and calculate log metrics."""
    total_size = 0
    status_codes = {}
    line_count = 0
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    pattern = (
        r'^(\S+) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(pattern, line.rstrip('\n'))

            if match:
                code = int(match.group(3))
                size = int(match.group(4))

                total_size += size

                if code in valid_codes:
                    status_codes[code] = (
                        status_codes.get(code, 0) + 1
                    )

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        if line_count % 10 != 0 or line_count == 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
