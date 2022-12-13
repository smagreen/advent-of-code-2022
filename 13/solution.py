def read_input(filename):
    with open(filename, encoding="utf8") as file:
        lines = file.read().splitlines()
        return [eval(line) for line in lines if len(line) > 0]

def is_ordered(left_packet, right_packet):
    result = None
    for lhs, rhs in zip(left_packet, right_packet):
        if isinstance(lhs, list) and isinstance(rhs, list):
            result = is_ordered(lhs,rhs)
            if result in ['Correct','Wrong']:
                break
        elif isinstance(lhs, list) and isinstance(rhs, int):
            result = is_ordered(lhs, [rhs])
            if result in ['Correct','Wrong']:
                break
        elif isinstance(lhs, int) and isinstance(rhs, list):
            result = is_ordered([lhs],rhs)
            if result in ['Correct','Wrong']:
                break
        else: # two integers
            if lhs < rhs:
                result = "Correct"
            elif lhs > rhs:
                result = "Wrong"
            else: result = "Equal"
            if result in ['Correct','Wrong']:
                break

    if result in ['Correct','Wrong']:
        return result
    # continue if still equal, must differ in length
    if len(left_packet) < len(right_packet):
        return 'Correct'
    if len(left_packet) > len(right_packet):
        return 'Wrong'
    return 'Equal'

def part_1(packets):
    results = []
    count = 0
    while len(packets):
        count+=1
        lhs = packets.pop()
        rhs = packets.pop()
        if is_ordered(lhs, rhs) == "Correct":
            results.append(count)
    return sum(results)

result_1 = part_1(read_input("./13/test.txt"))
print(f"Part 1: {result_1}, {'Pass' if result_1 == 13 else 'Fail'}")

result_2 = part_1(read_input("./13/input.txt"))
print(f"Part 1: {result_2}, {'Pass' if result_2 == 5905 else 'Fail'}")
