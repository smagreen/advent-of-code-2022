def read_instructions(filename):
    return [line.strip() for line in open(filename).readlines()]

def follow_instructions(instructions :list):
    root = './'
    current_dir = root
    directories = [current_dir]
    files = []

    for ins in instructions:
        if ins.startswith("$ cd .."):
            current_dir = current_dir[0 : current_dir.rindex('/')]
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
    for dir in directories:
        sizes = [(path, size) for path, _, size in files if path == dir]
        attribs.update({dir: sum(size for _, size in sizes)})
        
    return attribs

def solve(attribs):
    root = './'
    for path, size in attribs.items():
        if path == root: break
        parent = path[0 : path.rindex('/')]
        if len(parent) == 1: parent = root
        attribs[parent] += size

    part_1 = sum(size for _, size in attribs.items() if size <= 100000 )
    
    available = 70000000 - max(size for _, size in attribs.items())
    part_2 = sorted(size for _, size in attribs.items() if size >= 30000000 - available )[0]
    
    return part_1, part_2
 

instructions = read_instructions('./7/input.txt')
directories, files = follow_instructions(instructions)
attribs = calc_directory_size(directories, files)
print(solve(attribs) == (1432936, 272298))


    