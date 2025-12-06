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
        return [line.rstrip("\r\n") for line in file.readlines()]

def process_input(data: list[str])->tuple[list[bool], list[list[int]]]:
    """
    123 328      [["1"  , "23" , "356"],
     45 64        ["369", "248", "8"]]
      6 98   ->
    *   +        is_mul: [True, False]
    """
    operations_line, values_lines = data[-1], data[:-1]
    is_mul, values = [], []

    value_start, value_end = 0, None
    question_values = []
    for i, char in enumerate(operations_line):
        if char=="*":
            is_mul.append(True)
        elif char=="+":
            is_mul.append(False)

        question_value = "".join(line[i] for line in values_lines).strip()
        if not question_value:
            values.append(question_values)
            question_values = []
        else:
            question_values.append(int(question_value))
        # logger.info(f"{values}, {question_values}")
    if question_values:
        values.append(question_values)
    return is_mul, values

def main():
    # data = read_input("day6/example_input.txt")
    data = read_input("day6/input.txt")
    is_mul_list, values = process_input(data)
    logger.info(values)
    total = 0
    for is_mul, math_values in zip(is_mul_list, values):
        if is_mul:
            current_sum = prod(math_values)
        else:
            current_sum = sum(math_values)
        logger.info(f"{'*'  if is_mul else '+'} {math_values}: {current_sum}")
        total += current_sum
    logger.info(total)
    print(total)



if __name__ == "__main__":
    main()