def word_to_num(word):
    unit_map = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
    tens_map = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}

    if word in unit_map:
        return unit_map[word]
    elif word in tens_map:
        return tens_map[word]
    else:
        tens, unit = word.split('-')
        return tens_map[tens] + unit_map[unit]

input = open("input.txt", "r") # open file

total_sum = 0

for line in input:
    line = line.rstrip('\n')
    first_digit = None
    last_digit = None

    for word in line.split():
        if word.isdigit() or '-' in word or word in word_to_num:
            digit = word if word.isdigit() else str(word_to_num(word))
            if first_digit is None:
                first_digit = digit
            last_digit = digit

    if first_digit is not None and last_digit is None:
        last_digit = first_digit

    if first_digit is not None and last_digit is not None:
        total_sum += int(first_digit + last_digit)

print(total_sum)