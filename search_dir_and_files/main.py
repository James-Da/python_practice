import shutil
import re
import os
import time
from pathlib import Path
from datetime import datetime
from math import ceil

# Define the directory path where the files are located
directory_path = Path(os.getcwd(), "challenge_instructions", "My_Big_Directory")

# Get the current date in the desired format
today = datetime.now().strftime("%d-%m-%Y")


def extract_archive(source="Project+Day+9.zip"):
    """Extract the archive file to the specified directory."""
    shutil.unpack_archive(source, "challenge_instructions", "zip")


def find_serial_numbers():
    """Find and print the serial numbers from the files in the directory."""
    print(f"Search date: [{today}]")
    print("FILE            SERIAL NO.")
    pattern = "N[a-z]{3}-\d{5}"
    serial_numbers = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "r") as file:
                file_content = file.read()
                serial_number = re.search(pattern, file_content)

                if serial_number:
                    print(f"{file_name:<15} {serial_number.group()}")
                    serial_numbers.append(serial_number.group())

    print(f"Numbers found: {len(serial_numbers)}")


def measure_search_duration():
    """Measure and print the duration of the search operation."""
    time_start = time.time()
    find_serial_numbers()
    time_end = time.time()
    print(f"Search duration: {ceil(time_end - time_start)} seconds")


# Extract the archive file
extract_archive()

# Measure the search duration
measure_search_duration()
