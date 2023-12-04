from os import path, getcwd
import re

def main():
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day1_input"

  part1_calibration_values_sum = 0
  part2_calibration_values_sum = 0
  numbers_as_strings = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    for line in f:
      part1_digits = re.findall(r'\d{1}+', line)
      part2_search = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))+', line)
      for char in line:
        if char.isdigit():
          part1_digits.append(char)
      part1_calibration_values_sum += int(part1_digits[0] + part1_digits[-1])
      part2_digits = []
      for digit in part2_search:
        if digit in numbers_as_strings:
          part2_digits.append(numbers_as_strings[digit])
        else: part2_digits.append(digit)
      part2_calibration_values_sum += int(part2_digits[0] + part2_digits[-1])

  print(f"Sum of all part 1 calibration values are: {part1_calibration_values_sum}")
  print(f"Sum of all part 2 calibration values are: {part2_calibration_values_sum}")

if __name__=="__main__":
  main()