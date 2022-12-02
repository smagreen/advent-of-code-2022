
def part_1_unreadable():
    v={'X':1,'Y':2,'Z':3}
    return sum([3+v[r[2]] if r in ['A X','B Y','C Z']
        else 6+v[r[2]] if r in ['A Y','B Z','C X']
        else v[r[2]] for r in [l.strip() for l in open('./2/input.txt')]])

def part_2_unreadable():
    v,s={'X':1,'Y':2,'Z':3},{'X':0,'Y':3,'Z':6}
    return sum ([s[r[2]]+v[{'A':'Z','B':'X','C':'Y'}[r[0]]] if s[r[2]]==0 
                else s[r[2]]+v[{'A':'X','B':'Y','C':'Z'}[r[0]]] if s[r[2]]==3
                else s[r[2]]+v[{'A':'Y','B':'Z','C':'X'}[r[0]]]
                for r in [l.strip() for l in open('./2/input.txt')]])

print(f"Solve Part 1 - Unreadable = { part_1_unreadable() == 12586}") #12586
print(f"Solve Part 2 - Unreadable = { part_2_unreadable() == 13193 }") #13193
