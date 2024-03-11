with open('data.txt', 'r') as fin:
    lines = fin.readlines()

def debug_print(a):
    print(a, end=' ')
    return a

lengths = [debug_print(float(line.split('\t')[2])) for line in lines]
print()

net_force = float(input('Net Force: '))
net_length = sum(lengths)

print('Efficiency:', net_force / net_length)
print('Net Force:', net_force)
print('Net Length:', net_length)
