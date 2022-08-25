from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    count: int = 0
    k: int = 1

    while n > 0:
        if k > n:
            k = 1
        n -= k
        k += 1
        count += 1

    stdout.write("%d\n" % count)


if __name__ == "__main__":
    solution()
