INPUT_FILE = "input.txt"


def main():
    with open(INPUT_FILE, "r") as f:
        calibration_values_sum = 0
        for line in f.readlines():
            first_digit = ""
            last_digit = ""
            for char in line:
                if char.isdigit():
                    if first_digit == "":
                        first_digit = char
                    else:
                        last_digit = char

            if last_digit == "":
                last_digit = first_digit

            calibration_value = first_digit + last_digit
            calibration_values_sum += int(calibration_value)

        f.close()
    
    print(f"(Part 1) Calibration Values Sum: {calibration_values_sum}")


if __name__ == "__main__":
    main()
