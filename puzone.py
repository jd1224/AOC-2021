
def part_one():
    measurements = []
    inc = 0
    with open("2021/input.txt", 'r') as infile:
        measurements = infile.readlines()
        infile.close()
        prev = int(measurements[0])
        for m in measurements:
            if int(m) > prev:
                inc +=1
            prev = int(m)
        
    print(f'Increases: {inc}')

def part_two():
    with open("2021/input.txt", 'r') as infile:
        measurements = infile.readlines()
        intmeas = []
        count = 0
        for i in measurements:
            intmeas.append(int(i))
        for i in range(0,len(intmeas)-3):
            one = intmeas[i]
            two = intmeas[i+1]
            three = intmeas[i+2]
            four = intmeas[i+3]
            sumone = one+two+three
            sumtwo = two+three+four
            if sumone < sumtwo:
                count+=1
        print(count)

part_two()
