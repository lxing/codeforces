import sys
import string

args = raw_input().split()
m = int(args[0])
n = int(args[1])


def zero_row(A, r, n):
  for c in range(n):
    A[r][c] = 0

def zero_col(A, c, m):
  for r in range(m):
    A[r][c] = 0

def row_empty(A, r, n):
  for c in range(n):
    if A[r][c] == 1: return False
  return True

def col_empty(A, c, r):
  for r in range(m):
    if A[r][c] == 1: return False
  return True



A = []
B = []
for _ in range(m):
  ints = raw_input().split()
  A.append([1 for _ in ints])
  B.append([int(x) for x in ints])

for r in range(m):
  for c in range(n):
    if B[r][c] != 0: continue
    zero_row(A, r, n)
    zero_col(A, c, m)

for r in range(m):
  for c in range(n):
    if B[r][c] != 1: continue
    if row_empty(A, r, n) and col_empty(A, c, m):
      print 'NO'
      sys.exit()

print 'YES'
for row in A:
  print string.join([str(x) for x in row], ' ')
