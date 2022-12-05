def read_input(filename):
    lines = open(filename).readlines()

    base = [idx for idx, line in enumerate(lines) if line.startswith(' 1   2')][0]

    stacks = [l.replace('\n',' ') for l in lines[0 : base]]
    instructions = [(int(x[1]),int(x[3]),int(x[5])) for x in 
                    [line.strip().split() for line in lines[base + 2:]]]
    
    return stacks, instructions

def build_stacks(in_stacks):
    num_stacks = len(in_stacks[0]) // 4
    stack_height = len(in_stacks)
    stacks = [[] for _ in range(0, num_stacks)]
    
    stack_offsets = range(1, len(in_stacks[0]), 4)
    for stack_num, offset in enumerate(stack_offsets):
        for stack_idx in range(stack_height-1, -1, -1):
            crate = in_stacks[stack_idx][offset].strip()
            if len(crate) > 0:
                stacks[stack_num].append(crate)
        
    return stacks

def part_1_instructions(stacks, instructions):
    for instruction in instructions:
        moves, _from, to = instruction
        for _ in range(0, moves):
            crate = stacks[_from - 1].pop()
            stacks[to - 1].append(crate)

    return stacks

def part_2_instructions(stacks, instructions):
    for instruction in instructions:
        moves, _from, to = instruction
        crates = []
        for _ in range(0, moves):
            crate = stacks[_from - 1].pop()
            crates.append(crate)
        
        crates.reverse()
        stacks[to - 1] = stacks[to - 1] + crates
    
    return stacks

stack_string, instructions = read_input('./5/input.txt')
print([c[-1] for c in part_1_instructions(build_stacks(stack_string), instructions)])
print([c[-1] for c in part_2_instructions(build_stacks(stack_string), instructions)])
