from tqdm import tqdm

def rotate(current: int, direction: str, value: int):
    full_rotations, value = divmod(value, 100)
    if value == 0:
        return current, full_rotations
    if direction == "L":
        new_val=current-value
    elif direction == "R":
        new_val=current+value
    else:
        raise ValueError("Invalid direction")
    # special case, rotation to left from 0, shouldn't count click even if <= 0
    clicked = not(0<new_val<100) if current>0 else 0
    return new_val%100, full_rotations + clicked

def parse_input():
    with open("day1/input.txt") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def main():
    data = parse_input()
    state = 50
    password = 0
    for line in tqdm(data):
        if len(line) < 2:
            continue
        state, clicked = rotate(state, line[0], int(line[1:]))
        password += clicked
    print(password)


if __name__ == "__main__":
    main()