import math
import logging
from pathlib import Path
import numpy as np

from tqdm import tqdm
from functools import cache


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

def main():
    # data = read_input("day7/example_input.txt")
    data = read_input("day7/input.txt")
    beams_passing_through = [[0 for _ in line] for line in data] # beams_passing_through
    beams_passing_through[1][data[0].index('S')] = 1
    length = len(data[0])
    for i, (bpt, line) in enumerate(zip(beams_passing_through[1:-1], data[1:-1]), start=1):
        for j in range(length):
            if line[j]=="^":
                beams_passing_through[i][j-1] += beams_passing_through[i-1][j]
                beams_passing_through[i][j+1] += beams_passing_through[i-1][j]
            else:
                beams_passing_through[i][j] += beams_passing_through[i-1][j]

    print(sum(beams_passing_through[-2]))

if __name__ == "__main__":
    main()