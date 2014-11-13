import sys

args = raw_input().split()
a = int(args[0])
m = int(args[1])

memo = set()

while True:
  memo.add(a)
  a = (2*a) % m
  if a in memo:
    print 'No'
    sys.exit()
  if a == 0:
    print 'Yes'
    sys.exit()
