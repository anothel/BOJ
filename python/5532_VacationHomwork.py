from sys import stdin, stdout


def main():
  L: int = int(stdin.readline().rstrip())
  A: int = int(stdin.readline().rstrip())
  B: int = int(stdin.readline().rstrip())
  C: int = int(stdin.readline().rstrip())
  D: int = int(stdin.readline().rstrip())

  stdout.write(str(L - max(B//D if B % D == 0 else B //
               D + 1, A//C if A % C == 0 else A//C + 1)))


if __name__ == "__main__":
    main()
