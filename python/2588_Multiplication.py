import sys

data = [sys.stdin.readline().strip() for i in range(2)]

x1 = int(data[0])
x2 = int(data[1])

print(x1*(x2 % 10))
print(x1*int((x2/10) % 10))
print(x1*int(x2/100))
print(x1*x2)
