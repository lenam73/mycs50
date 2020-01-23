import sys

# while True:
#     n = int(input("Height: "))
#     if 1 <= n <= 8:
#         break
n = 8
for i in range(1, n):
    k = n - i
    for j in range(1, n):
        if j > k:
            sys.stdout.write('#')
        else:
            sys.stdout.write(" ")
    sys.stdout.write('  ')
    for j in range(1, i):
        sys.stdout.write('#')
    sys.stdout.write("\n")
