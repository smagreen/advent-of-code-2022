import re
def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def run(instructions):
    x = 1
    x_values = [x]
    pixels = ['.'] * 240

    for line in instructions:
        x_values.append(x)
        if re.search("\d", line):
            x += int(line.split()[1])
            x_values.append(x)

    part_1 = sum([ check * x_values[check - 1] for check in [20,60,100,140,180,220]])

    for pixel in range(0, 240):
        line_pixel = pixel % 40
        if line_pixel - 1 <= x_values[pixel] <= line_pixel + 1:
            pixels[pixel] = '#'
    
    return part_1, pixels

part_1, pixels = run(read_input('./10/input.txt'))

print(part_1)

print(''.join(pixels[0:40]))
print(''.join(pixels[40:80]))
print(''.join(pixels[80:120]))
print(''.join(pixels[120:160]))
print(''.join(pixels[160:200]))
print(''.join(pixels[200:240]))
    
