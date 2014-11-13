import sys

args = raw_input().split()
m = int(args[0])
n = int(args[1])

A = []
B = []
for _ in range(m):
  ints = raw_input().split()
  A.append([0 for _ in ints])
  B.append([int(x) for x in ints])

print A, B
