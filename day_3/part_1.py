INPUT_FILE = "input.txt"
ADJ_INDICES = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def main():
    with open(INPUT_FILE, "r") as f:
        matrix = []
        for line in f.readlines():
            matrix.append(line)
        f.close()

    part_num_sum = 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if is_symbol(char):
                for indices in ADJ_INDICES:
                    p = i + indices[0]
                    q = j + indices[1]
                    if p < 0 or p >= len(matrix) or q < 0 or q >= len(matrix[p]) or not matrix[p][q].isdigit():
                        continue
                    
                    while matrix[p][q].isdigit():
                        # Walk the pointer backwards until the beginning of the number is reached
                        q -= 1
                        if q == -1:
                            break
                    q += 1

                    part_num_str = ""
                    while matrix[p][q].isdigit():
                        # Retrieve the current digit
                        part_num_str += matrix[p][q]

                        # Replace the current digit with a period to ensure it's not counted multiple times
                        new_str = list(matrix[p])
                        new_str[q] = "."
                        matrix[p] = "".join(new_str)

                        # Advance the pointer
                        q += 1
                        if q >= len(matrix[p]):
                            break
                    
                    part_num_sum += int(part_num_str)
    
    print(f"(Part 1) Part Number Sum: {part_num_sum}")


def is_symbol(string: str) -> bool:
    return not string.isdigit() and not string.isspace() and string != "."


if __name__ == "__main__":
    main()
