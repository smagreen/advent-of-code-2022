def read_input(filename):
    calories = []
    total = 0

    with open(filename) as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            if len(line.strip()) == 0 or idx == len(lines) - 1:
                calories.append(total)
                total = 0
            else:
                total += int(line.strip())

    return calories

def part_1(calories):
    return max(calories)

def part_2(calories):
    calories.sort(reverse=True)
    return sum(calories[0:3])

calories = read_input("./1/input.txt")

# Part 1 = 69501
print(part_1(calories))
    
# Part 2 = 202346
print (part_2(calories))


