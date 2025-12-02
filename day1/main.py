from tqdm import tqdm

def rotate(current: int, direction: str, value: int):
    if direction == "L":
        current-=value
    elif direction == "R":
        current+=value
    return current%100

def parse_input():
    with open("day1/input.txt") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def main():
    data = parse_input()
    state = 50
    password = 0
    print(50)
    for line in tqdm(data):
        if len(line) < 2:
            continue
        # print(line, line[0], line[1:])
        state = rotate(state, line[0], int(line[1:]))
        # print(line, "->", state)
        password += state == 0
    print(password)


if __name__ == "__main__":
    main()