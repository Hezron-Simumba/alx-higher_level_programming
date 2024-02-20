#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

# Function to handle CTRL+C interruption
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Function to print statistics
def print_statistics():
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count:
            print(f"{code}: {count}")

# Attach the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update total size and status code count
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle any other keyboard interruption
    print_statistics()
    sys.exit(0)

