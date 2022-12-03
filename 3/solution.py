def read_input(filename):
    return [line.strip() for line in open(filename)]

def calc_priority(c):
    return ord(c)-96 if c.islower() else ord(c)-38

def part_1(rucksacks):
    return sum([calc_priority(
                list(
                    set(items[0:int(len(items)/2)]) &
                    set(items[int(len(items)/2):])
                )[0])
            for items in rucksacks])

def part_2(rucksacks):
    return sum([calc_priority(
                list(
                    set(rucksacks[x]) &
                    set(rucksacks[x+1]) &
                    set(rucksacks[x+2])
                )[0])
            for x in range(0, len(rucksacks), 3)])

test_data = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]

print (part_1(test_data) == 157 )
print (part_1(read_input('./3/input.txt')) == 8018)
print (part_2(test_data) == 70 )
print (part_2(read_input('./3/input.txt')) == 2518)