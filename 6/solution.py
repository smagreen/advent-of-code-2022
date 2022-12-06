def find_marker(line, marker_length=4):
    for idx in range(0, len(line)):
        slc = slice(idx, idx + marker_length)
        marker_set = set(line[slc])
        if len(marker_set) == marker_length: return idx + marker_length

def find_marker_golf(l, ml=4):
     return [ i + ml for i in range(0, len(l))
         if len(set(l[slice(i, i + ml)])) == ml][0]

#Tests
print(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')== 5)
print(find_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6)
print(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10)
print(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11)

print(find_marker(open("./6/input.txt").readline()) == 1848)
print(find_marker(open("./6/input.txt").readline(), 14) == 2308)

print(find_marker_golf(open("./6/input.txt").readline()) == 1848)
print(find_marker_golf(open("./6/input.txt").readline(), 14) == 2308)

    
    


