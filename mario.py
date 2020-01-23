import sys

while True:
    try:
        n = int(input("Height: "))
    except ValueError:
        continue
    if 1 <= n <= 8:
        break

for i in range(1, n + 1):
    k = n - i
    for j in range(1, n + 1):
        if j > k:
            sys.stdout.write('#')
        else:
            sys.stdout.write(" ")
    sys.stdout.write('  ')
    for j in range(1, i + 1):
        sys.stdout.write('#')
    sys.stdout.write("\n")
