from math import prod
import logging
from pathlib import Path
from functools import reduce
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

def process_input(data: list[str]):
    values, operations = [list(map(int, line.split())) for line in data[:-1]], data[-1].split()
    return values, operations

def main():
    # data = read_input("day6/example_input.txt")
    data = read_input("day6/input.txt")
    values, operations = process_input(data)
    # print(values)
    # print(operations)
    total = 0
    for x in zip(operations, *values):
        x = list(x)
        operation, nums = x[0], x[1:]
        if operation == "*":
            current_sum = prod(nums)
        else:
            current_sum = sum(nums)
        logger.info(f"{operation} {nums}: {current_sum}")
        total += current_sum
    logger.info(total)
    print(total)



if __name__ == "__main__":
    main()