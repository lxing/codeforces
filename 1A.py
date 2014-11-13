args = raw_input().split()

n = int(args[0])
m = int(args[1])
a = int(args[2])

na = n/a + (1 if n % a > 0 else 0)
ma = m/a + (1 if m % a > 0 else 0)

print na * ma