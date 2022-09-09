from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())
    tmp: str = str(n) * n
    if len(tmp) > m:
        stdout.write("%s" % tmp[:m])
    else:
        stdout.write("%s" % tmp)


if __name__ == "__main__":
    solution()