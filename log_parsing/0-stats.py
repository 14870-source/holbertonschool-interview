#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys


def print_statistics(total_file_size, status_counts):
    """Print accumulated file size and status code counts."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Process log lines from stdin."""
    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                try:
                    total_file_size += int(parts[-1])
                except ValueError:
                    pass
                try:
                    code = int(parts[-2])
                    if code in status_counts:
                        status_counts[code] += 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        raise

    print_statistics(total_file_size, status_counts)


if __name__ == "__main__":
    main()
