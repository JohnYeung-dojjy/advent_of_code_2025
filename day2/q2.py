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
        return file.readlines()[0].split(',')

def process_input(input_data: list[str])->list[tuple[str, str]]:
    """process input such that every start and end have the same number of digits"""
    processed_input = []
    for line in tqdm(input_data, desc="Processing raw input"):
        start, end = line.split('-')
        sl, el = len(start), len(end)
        if sl==el:
            processed_input.append((start, end)) # e.g. 10-56
        else:
            # from observing the input, 'end''s digit will have at most 1 more digit
            # if that's the case, break them apart
            if sl>=2:
                processed_input.append((start     , '9'*sl)) # e.g. 10-99
            processed_input.append(('1'+'0'*sl, end   )) # e.g. 100-123
    return processed_input

@cache
def get_factors(num)->list[int]:
    """Return the length of potential digit pattern"""
    # 1,len(num) is a factor, but we don't want len(num)
    factors = {1}
    for divisor in range(2, math.floor(math.sqrt(num))+1):
        q, r = divmod(num, divisor)
        if r==0:
            factors.add(q)
            factors.add(divisor)
    return list(factors)

def gen_invalid_id_candidates(start: str, end: str, factor: int):
    # start and end have the same length
    repeats = len(start)//factor
    start, end = int(start[:factor]), int(end[:factor])
    for num in range(start, end+1):
        yield str(num)*repeats

def main():
    # input_data = read_input('day2/example_input.txt')
    input_data = read_input('day2/input.txt')
    processed_input = process_input(input_data)
    invalid_id_sum = 0
    tested_candidates = set() # avoid repeated counts
    for line_num, (start, end) in tqdm(enumerate(processed_input), desc="Processing lines"):
        for factor in get_factors(len(start)):
            logger.info(f"processing {start} to {end}")
            logger.info(f"testing len={factor}")
            for candidate in gen_invalid_id_candidates(start, end, factor):
                if candidate in tested_candidates:
                    logger.info(f"\t{candidate} existed")
                    continue
                if start<=candidate<=end:
                    logger.info(f"\t{candidate} o")
                    invalid_id_sum += int(candidate)
                    tested_candidates.add(candidate)
                else:
                    logger.info(f"\t{candidate} x")
        logger.info(f"finished processing {start} to {end}")

    logger.info(f"ans: {invalid_id_sum}")
    print(f"ans: {invalid_id_sum}")

if __name__ == "__main__":
    main()
