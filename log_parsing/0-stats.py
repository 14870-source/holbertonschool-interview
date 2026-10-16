
#!/usr/bin/python3
"""Parse log lines and print accumulated metrics."""

import sys
import re


def print_stats(total_size, status_codes):
    """Print the total file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read stdin and compute log metrics."""
    total_size = 0
    status_codes = {}
    line_count = 0
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    pattern = (
        r'^(\S+) - \[.*?\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.rstrip('\n')
            match = re.match(pattern, line)

            if match:
                code = int(match.group(2))
                size = int(match.group(3))

                if code in valid_codes:
                    total_size += size
                    status_codes[code] = status_codes.get(code, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        if line_count % 10 != 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
