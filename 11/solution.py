import time
import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s")

# Create a class to represent a monkey
class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []  
        self.operation = ''
        self.divisible_by = None
        self.if_true = None
        self.if_false = None
        self.items_inspected = 0
    
    def items_to_throw(self, divide_by_three=False, max_worry=1):
        s = self.operation.split()
        operator = s[-2]
        op_value = s[-1]

        throw_items = []

        self.items_inspected += len(self.items)
        for item in self.items:

            if operator == '+':
                item += int(op_value)
            elif op_value == 'old':
                item *= item
            else: item *= int(op_value)
            
            item = item // 3 if divide_by_three else item % max_worry
            target = item % self.divisible_by
            next_monkey = self.if_true if target == 0 else self.if_false 
            throw_items.append((next_monkey, item))
        
        self.items = []
        return throw_items

    def __str__(self) -> str:
        return f"Monkey: {self.id}, inspected:{self.items_inspected}, items: {self.items}"



def read_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    monkeys = []
    for line in lines:
        if line.startswith('Monkey '):
            this_monkey = Monkey(len(monkeys))
        if line.startswith('Starting items:'):
            this_monkey.items = list(map(int,line[16:].strip().split(', ')))
        if line.startswith('Operation:'):
            this_monkey.operation = line[11:].strip()
        if line.startswith('Test: divisible by '):
            this_monkey.divisible_by = int(line[19:].strip())
        if line.startswith('If true: throw to monkey '):
            this_monkey.if_true = int(line[25:].strip())
        if line.startswith('If false: throw to monkey '):
            this_monkey.if_false = int(line[25:].strip())
            monkeys.append(this_monkey)

    return monkeys

def solve(monkeys, num_rounds, divide=True):
    logging.info(f"Starting solve: {num_rounds}, Part {1 if divide else 2}")
    start = time.perf_counter()
    max_worry = 1
    for m in monkeys:
        max_worry *= m.divisible_by

    for round in range(num_rounds):
        for monkey in monkeys:
            thrown = monkey.items_to_throw(divide, max_worry)
            for target, wl in thrown:
                monkeys[target].items.append(wl)

    totals = sorted([m.items_inspected for m in monkeys], reverse=True)
    
    end = time.perf_counter()
    logging.info(f"Solve: {num_rounds}, Time: {end - start:0.4f} secs \n\tMonkey Items: {totals}")

    return totals[0] * totals[1]


test_monkeys = read_input('./11/test.txt')
part_1_test = solve(test_monkeys, 20) 
print(f"Test Pass = {part_1_test==10605}")

monkeys = read_input('./11/input.txt')
part_1 = solve(monkeys, 20, True) 
print(f"Pass = {part_1 == 66124}, {part_1}")

monkeys = read_input('./11/input.txt')
part_2 = solve(monkeys, 10000, False) 
print(f"Pass = {part_2 == 19309892877}, {part_2}")




