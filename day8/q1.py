import math
import logging
from pathlib import Path
import numpy as np

from tqdm import tqdm
from collections import defaultdict
np.set_printoptions(linewidth=np.inf)


LOG_FILE = Path(__file__).with_name("processing.log")
logging.basicConfig(
    filename=LOG_FILE,
    filemode="w",
    level=logging.INFO,
    # format="%(asctime)s - %(levelname)s - %(message)s",
    format="%(message)s",
)

logger = logging.getLogger(__name__)



class JunctionBox:
    def __init__(self, xyz: list[int]):
        self.xyz = np.array(xyz)

    def distance(self, other: "JunctionBox"):
        return np.linalg.norm(self.xyz - other.xyz)

    def __repr__(self):
        return str(self.xyz)

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def create_distance_matrix(junction_boxes: list[JunctionBox]):
    n = len(junction_boxes)
    distances = np.array([[np.inf for _ in range(n)] for _ in range(n)])
    for i, a in enumerate(junction_boxes[:-1]):
        for j, b in enumerate(junction_boxes[i+1:], start=i+1):
            distances[i,j] = a.distance(b)
    return distances



def main():
    input_path = "day8/example_input.txt"
    input_path = "day8/input.txt"
    data = read_input(input_path)
    n = len(data)
    group_map: list[int] = np.array([i for i in range(n)])
    junction_boxes = [JunctionBox(list(map(int, line.split(",")))) for line in data]
    distances = create_distance_matrix(junction_boxes)
    # logger.info(distances//1)
    def connect(a: int, b: int):
        logger.info(f"connecting {junction_boxes[a]}, {junction_boxes[b]} to group {group_map[a]}")
        if a!=b:
            group_map[group_map==group_map[b]] = group_map[a]
        distances[a,b]=np.inf

    # logger.info(group_map)
    iters = n//2 if "example" in input_path else n
    for _ in tqdm(range(iters)):
        connect(*divmod(np.argmin(distances), n))
        # logger.info(group_map)

    group_count = defaultdict(int)
    for group in group_map:
        group_count[group] += 1
    group_count = sorted(group_count.items(), reverse=True, key=lambda x: x[1])
    res = 1
    for i in range(3):
        logger.info(group_count[i])
        res *= group_count[i][1]
    logger.info(res)
    print(res)

if __name__ == "__main__":
    main()