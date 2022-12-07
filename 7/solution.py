def read_instructions(filename):
    instructions = [line.strip() for line in open(filename).readlines()]
    return instructions

def follow_instructions(instructions):
    root = './'
    current_dir = root
    directories = [current_dir]
    files = []

    for ins in instructions:
        if ins.startswith("$ cd .."):
            last_slash = current_dir.rindex('/')
            current_dir = current_dir[0 : last_slash]
        elif ins == '$ cd /':
            current_dir = root
        elif ins.startswith('$ cd '):
            change_to = ins[5:]
            if current_dir == root:
                current_dir += change_to
            else:
                current_dir += '/' + change_to
        elif ins.startswith('$ ls'):
            pass
        elif ins.startswith('dir '):
            directory = ins[4:]
            directories.append(f"{current_dir}{'' if current_dir == root else '/'}{directory}")
        else :
            size, filename = ins.split()
            files.append((current_dir, filename, int(size)))
            
    return directories, files

def calc_directory_size(directories, files):
    directories.sort(key=len, reverse=True)
    attribs = {}
    for d in directories:
        sizes = [(s[0], s[2]) for s in files if s[0] == d]
        attribs.update({d: sum(size for _, size in sizes)})
        
    return attribs

def solve(attribs):
    root = './'
    for key, value in attribs.items():
        if key == root: break
        if value > 0 :
            parent = key[0 : key.rindex('/')]
            if len(parent) == 1: parent = root
            attribs[parent] += value

    part_1 = sum([dir[1] for dir in attribs.items() if dir[1] <= 100000 ])
    
    available = 70000000 - max(dir[1] for dir in attribs.items())
    part_2 = sorted([dir[1] for dir in attribs.items() if dir[1] >= 30000000 - available ])[0]
    
    return part_1, part_2
 

instructions = read_instructions('./7/input.txt')
directories, files = follow_instructions(instructions)
attribs = calc_directory_size(directories, files)
print(solve(attribs) == (1432936,272298))


    