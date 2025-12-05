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
    n = len(bank)
    max_battery_idx_until_i = [-1 for _ in bank]
    max_battery_idx_until_i[0] = 0
    max_battery_idx_to_right = [-1 for _ in bank]
    max_battery_idx_to_right[-1] = n-1
    for i, battery in enumerate(bank[1:], start=1):
        j = n-i-1
        if bank[i]>bank[max_battery_idx_until_i[i-1]]:
            max_battery_idx_until_i[i] = i
        else:
            max_battery_idx_until_i[i] = max_battery_idx_until_i[i-1]
        if bank[j]>bank[max_battery_idx_to_right[j+1]]:
            max_battery_idx_to_right[j]=j
        else:
            max_battery_idx_to_right[j]=max_battery_idx_to_right[j+1]
    max_joltage = 0
    for i in range(n-1):
        joltage = int(bank[max_battery_idx_until_i[i]])*10 + int(bank[max_battery_idx_to_right[i+1]])
        max_joltage = max(max_joltage, joltage)
    logger.info(bank)
    logger.info(max_battery_idx_until_i)
    logger.info(max_battery_idx_to_right)
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