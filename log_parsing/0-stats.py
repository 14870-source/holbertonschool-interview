#!/usr/bin/python3
"""Read log lines and compute metrics."""

import sys
import re


def print_stats(total_size, status_codes):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read stdin and calculate log metrics."""
    total_size = 0
    status_codes = {}
    line_count = 0

    pattern = (
        r'^(\d{1,3}(?:\.\d{1,3}){3}) - '
        r'\[([^\]]+)\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    valid_codes = (200, 301, 400, 401, 403, 404, 405, 500)

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(pattern, line.rstrip('\n'))

            if match:
                code_text = match.group(3)
                size_text = match.group(4)

                code = int(code_text)
                size = int(size_text)
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
