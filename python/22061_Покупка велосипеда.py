from sys import stdin, stdout


def main():
    for _ in range(int(stdin.readline().rstrip())):
        r1, r2, b = map(int, stdin.readline().strip().split())
        r2 *= 2
        if r2 > b and (b % 2) == 0:
            stdout.write("YES\n")
        elif r2 > b and (b % 2) != 0:
            if r1 >= 1:
                stdout.write("YES\n")
            else:
                stdout.write("NO\n")
        elif r2 == b:
            stdout.write("YES\n")
        elif r2 < b:
            if b-r2 <= r1:
                stdout.write("YES\n")
            else:
                stdout.write("NO\n")


if __name__ == "__main__":
    main()
