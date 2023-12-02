import re
from typing import Tuple

INPUT_FILE = "input.txt"
REGEX_PATTERN = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"


def main():
    with open(INPUT_FILE, "r") as f:
        calibration_values_sum = 0
        for line in f.readlines():
            calibration_value = get_calibration_value_from_line(line)
            calibration_values_sum += calibration_value

        f.close()

    print(f"(Part 2) Calibration Values Sum: {calibration_values_sum}")


def get_calibration_value_from_line(line: str) -> int:
    first_digit, last_digit = get_calibration_digits_from_line(line)
    calibration_value = int(first_digit + last_digit)

    return calibration_value


def get_calibration_digits_from_line(line: str) -> Tuple[str, str]:
    line = line.lower()
    m = re.finditer(REGEX_PATTERN, line)
    results = [_m.group(1) for _m in m]
    first_digit = ""
    last_digit = ""
    if len(results) < 1:
        raise RuntimeError("Unable to find digits")
    elif len(results) == 1:
        first_digit = results[0]
        last_digit = first_digit
    else:
        first_digit = results[0]
        last_digit = results[-1]

    if not first_digit.isdigit():
        first_digit = convert_word_to_digit(first_digit)
    if not last_digit.isdigit():
        last_digit = convert_word_to_digit(last_digit)

    return first_digit, last_digit


def convert_word_to_digit(word: str) -> str:
    word = word.lower()
    ret = ""
    if word == "one":
        ret = "1"
    if word == "two":
        ret = "2"
    if word == "three":
        ret = "3"
    if word == "four":
        ret = "4"
    if word == "five":
        ret = "5"
    if word == "six":
        ret = "6"
    if word == "seven":
        ret = "7"
    if word == "eight":
        ret = "8"
    if word == "nine":
        ret = "9"
    
    return ret


if __name__ == "__main__":
    main()
