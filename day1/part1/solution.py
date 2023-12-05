input = open("input.txt", "r") # open file

total_sum = 0

for line in input:
    line = line.rstrip('\n')
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char

    if first_digit is not None and last_digit is None:
        last_digit = first_digit

    if first_digit is not None and last_digit is not None:
        total_sum += int(first_digit + last_digit)

print(total_sum)