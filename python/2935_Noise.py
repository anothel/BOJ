import sys


def main():
  A = int(sys.stdin.readline())
  op = sys.stdin.readline()
  B = int(sys.stdin.readline())

  if op == "+\n":
    print(A+B)
  else:
    print(A*B)


if __name__ == "__main__":
    main()
