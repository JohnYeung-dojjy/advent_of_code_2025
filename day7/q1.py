import math
import logging
from pathlib import Path
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

class TachyonManifold:
    def __init__(self, map: list[str]):
        self.map = map
        self.split_count = 0

    def split(self, beam: tuple[int, int]):
        self.split_count+=1
        r, c = beam
        return {(r+1, c-1), (r+1, c+1)}

    def fall(self):
        beams = {(0, self.map[0].index("S"))}
        for row in self.map[1:-1]:
            next_beams = set()
            # print(beams)
            for beam in beams:
                br, bc = beam
                if self.map[br+1][bc]=="^":
                    next_beams |= self.split(beam)
                else:
                    next_beams.add((br+1, bc))
            beams = next_beams

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    # data = read_input("day7/example_input.txt")
    data = read_input("day7/input.txt")
    TM = TachyonManifold(data)
    TM.fall()
    print(TM.split_count)

if __name__ == "__main__":
    main()