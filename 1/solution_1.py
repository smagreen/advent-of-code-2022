def read_input(filename):
    with open(filename) as f:
        return [int(n.strip()) if len(n.strip()) > 0 else 0 for n in f.readlines() ]

def build_calorie_list(input):
    elf_idx = 0
    calories = [0 for line in input if line == 0]
    calories.append(0)

    for line in input:
        if line == 0:
            elf_idx += 1
        else:
            calories[elf_idx] += line

    return calories

def part_1(calories):
    return max(calories)

def part_2(calories):
    calories.sort(reverse=True)
    return sum(calories[0:3])

calories = build_calorie_list(read_input("./1/input.txt"))

# Part 1 = 696501
print(part_1(calories))
    
# Part 2 = 202346
print (part_2(calories))


