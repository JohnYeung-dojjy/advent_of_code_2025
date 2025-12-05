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

def process_input(input_data: list[str])->tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ingredient_ids = []
    is_ranges=True
    for line in input_data:
        if line == "":
            is_ranges = False
            continue
        if is_ranges:
            ranges.append(tuple(map(int, line.split('-'))))
        else:
            ingredient_ids.append(int(line))
    return ranges, ingredient_ids


def main():
    # data = read_input("day5/example_input.txt")
    data = read_input("day5/input.txt")
    ranges, ingredient_ids = process_input(data)
    print(ranges)
    print(ingredient_ids)
    fresh_ids = 0
    for ingredient_id in ingredient_ids:
        for start, end in ranges:
            if start<=ingredient_id<=end:
                fresh_ids+=1
                break
    print(fresh_ids)


if __name__ == "__main__":
    main()