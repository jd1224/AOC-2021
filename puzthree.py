
def part_one(file):
    bits = {1:0,2:0,3:0,4:0,5:0}
    line_count = 0
    with open(file, 'r') as infile:
        lines = infile.readlines()
        for i in lines:
            line_count+=1
            for j in range(len(i.rstrip())):
                bits[int(j)+1]+=int(i[j])
    gamma = []
    epsilon = []
    for num in bits:
        if bits[num]/line_count>0.5:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(bin(int(''.join(map(str,gamma)), 2)<<1))
    print(bin(int(''.join(map(str,epsilon)), 2)<<1))
part_one("Inputs/test.txt")