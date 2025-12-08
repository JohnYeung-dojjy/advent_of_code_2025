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
        group_map[group_map==group_map[b]] = group_map[a]


    # logger.info(group_map)
    while len(np.unique(group_map))>=2:
        jb1, jb2 = divmod(np.argmin(distances), n)
        if group_map[jb1]==group_map[jb2]:
            distances[jb1,jb2]=np.inf
            continue
        if len(np.unique(group_map))==2:
            logger.info(np.unique(group_map))
            logger.info(f"{junction_boxes[jb1].xyz[0]}, {junction_boxes[jb2].xyz[0]}")
            res = junction_boxes[jb1].xyz[0] * junction_boxes[jb2].xyz[0]
            print(res)
            break
        connect(jb1, jb2)
        distances[jb1,jb2]=np.inf
        # logger.info(group_map)



if __name__ == "__main__":
    main()