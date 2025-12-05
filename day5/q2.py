import math
import logging
from pathlib import Path
from functools import cache
import numpy as np

from tqdm import tqdm

LOG_FILE = Path(__file__).with_name("processing.log")
logging.basicConfig(
    filename=LOG_FILE,
    filemode="w",
    level=logging.INFO,
    # format="%(asctime)s - %(levelname)s - %(message)s",
    format="%(message)s",
)

logger = logging.getLogger(__name__)

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def process_input(input_data: list[str])->list[tuple[int, int]]:
    ranges = []
    for line in input_data:
        if line == "":
            break
        ranges.append(tuple(map(int, line.split('-'))))
    return ranges

def merge_ranges(ranges: list[tuple[int, int]]):
    ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges, ranges = [ranges[0]], ranges[1:]
    # cases
    # 1. O----O
    #      O----O
    # 2. O----O
    #      O-O
    # 3. O--O
    #         O---O
    for start, end in ranges:
        last_start, last_end = merged_ranges[-1]
        if start > last_end:
            merged_ranges.append((start, end))
        else:
            merged_ranges.pop()
            merged_ranges.append((
                min(start, last_start),
                max(end, last_end)
            ))
    return merged_ranges

def main():
    # data = read_input("day5/example_input.txt")
    data = read_input("day5/input.txt")
    ranges = process_input(data)
    ranges = merge_ranges(ranges)
    # print(ranges)
    fresh_ids = 0
    for start, end in ranges:
        fresh_ids += end-start+1
    print(fresh_ids)


if __name__ == "__main__":
    main()