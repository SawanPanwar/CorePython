n = 4

s = 1

for i in range(1, 10, 2):

    for k in range(n, 0, -1):
        print(end="\t")

    n = n - 1

    for j in range(1, i + 1):
        print(s, end="\t")

    s = s + 1

    print()
    print()


# n, s = 4, 1
#
# for i in range(1, 10, 2):
#     print("\t" * n + ("\t".join([str(s)] * i)))
#     n -= 1
#     s += 1
#     print()

