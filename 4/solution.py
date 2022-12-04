def read_input(filename):
    return [(x[0].split('-'), x[1].split('-')) for x in [p.strip().split(',') for p in open(filename)]]

def count_contained_pair(lines):
    contained=0;
    intersects=0;
    for line in lines:
        lhs = set(range(int(line[0][0]), int(line[0][1])+1))
        rhs = set(range(int(line[1][0]), int(line[1][1])+1))
        intersect = lhs & rhs
        if len(intersect) > 0: intersects += 1
        if len(intersect) == len(lhs) or len(intersect) == len(rhs) : contained += 1

    return intersects, contained

input = read_input("./4/input.txt")
print(count_contained_pair(input) == (823, 431))