import logging
from pathlib import Path

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

def get_starting_number(start, end):
    start_even, end_even = len(start)%2==0, len(end)%2==0
    if start_even:
        # start is 77
        digits = len(start)
        first_half = digits//2
        begin = int(start[:first_half])
        if not end_even:
            # end is 110, make it 100
            end = str(10**digits)
    elif end_even:
        # end is 99
        digits = len(end)
        start = str(10**(digits-1))
        first_half = digits//2
        begin = 10**(first_half-1)
    else:
        # both are odd digits, can't form invalid id. Also from the input file.
        raise ValueError()
    return start, end, begin, first_half

def main():
    # input_data = read_input('day2/example_input.txt')
    input_data = read_input('day2/input.txt')
    invalid_id_sum = 0
    for line_num, line in tqdm(enumerate(input_data), desc="Processing lines"):
        start, end = line.split('-')
        try:
            start, end, begin, first_half = get_starting_number(start, end)
        except ValueError:
            continue
        if start is None:
            logger.info(f"processing {line_num+1}th")
            logger.info(f"{line}, odd number digit")
            logger.info("----")
            continue
        invalid_id = begin * (10**first_half + 1)
        if str(invalid_id) < start:
            # eg start,end = 3456,4000. And invalid_id is 3434
            # we make it start with 3535
            begin += 1
            invalid_id = begin * (10**first_half + 1)
        logger.info(f"processing {line_num+1}th")
        logger.info(start)
        start, end = int(start), int(end)
        while int(start) <= invalid_id <= int(end):
            logger.info(f'\t{invalid_id}')
            invalid_id_sum += invalid_id
            begin += 1
            invalid_id = begin * 10**first_half + begin
        logger.info(end)
        logger.info("----")
    logger.info(f"ans: {invalid_id_sum}")

if __name__ == "__main__":
    main()
