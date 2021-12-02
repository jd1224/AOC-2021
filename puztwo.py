def part_one(file):
    measurements = {'forward':0,'down':0,'up':0}
    with open(file, 'r') as infile:
        for line in infile.readlines():
            reading = line.split()
            measurements[reading[0]] += int(reading[1])
    horizontal = measurements['forward']
    vertical = measurements['down'] - measurements['up']
    print(horizontal*vertical)

def part_two(file):
    measurements = {'horizontal':0,'aim':0,'vertical':0}
    with open(file, 'r') as infile:
        for line in infile.readlines():
            reading = line.split()
            move = int(reading[1])
            if reading[0] == 'forward':
                
                measurements['horizontal'] += move
                measurements['vertical'] += move*measurements['aim']
            elif reading[0] == 'up':
                measurements['aim'] -= move
            else:
                measurements['aim'] += move
        print(measurements['horizontal']*measurements['vertical'])
part_two('2021/input.txt')