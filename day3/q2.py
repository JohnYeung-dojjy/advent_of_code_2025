import math
import logging
from pathlib import Path
from functools import cache

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

def find_max_joltage_in_bank(bank: str)->int:
    """Greedy"""
    logger.info(bank)
    n = len(bank)
    bank_list = list(bank)
    max_joltage = 0
    joltage_idxs = []
    last_idx = 0
    for i in range(1, 13):
        search_range = bank_list[last_idx:n-(12-i)]
        max_joltage_idx = last_idx + search_range.index(max(search_range))
        logger.info(f"{search_range}, {bank[max_joltage_idx]}, {max_joltage_idx}")
        last_idx = max_joltage_idx+1
        joltage_idxs.append(max_joltage_idx)
    for joltage_idx in joltage_idxs:
        max_joltage = (max_joltage+int(bank_list[joltage_idx]))*10
    max_joltage = max_joltage//10
    logger.info(max_joltage)
    logger.info("----")
    return max_joltage

def main():
    # banks = read_input("day3/example_input.txt")
    banks = read_input("day3/input.txt")
    total_output_joltage = 0
    for bank in banks:
        output_joltage = find_max_joltage_in_bank(bank)
        total_output_joltage += output_joltage
    logger.info(total_output_joltage)
    print(total_output_joltage)

if __name__ == "__main__":
    main()