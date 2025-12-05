import math
import logging
from pathlib import Path
from functools import cache
import numpy as np

from tqdm import tqdm
from scipy.signal import convolve2d

KERNEL = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

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

def process_input(input_data: list[str]):
    output = []
    for line in input_data:
        output.append(list(map(lambda x: x=='@', line)))
    return np.array(output).astype(int)

def main():
    # data = read_input("day4/example_input.txt")
    data = read_input("day4/input.txt")
    processed_data = process_input(data)
    # print(processed_data)
    total_rolls_removed = 0
    iter_limit = 1000
    while True and iter_limit>0:
        output = (convolve2d(processed_data, KERNEL, mode="same")<4) & processed_data
        processed_data[output==1]=0
        rolls_removed = output.sum()
        iter_limit-=1
        if iter_limit<=0:
            break
        if rolls_removed==0:
            break
        # print(rolls_removed)
        total_rolls_removed += rolls_removed
        # print(output.astype(int))
    print(total_rolls_removed)


if __name__ == "__main__":
    main()