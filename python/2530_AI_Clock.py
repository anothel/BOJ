import sys


def main():
  A, B, C = map(int, input().split())
  C += int(sys.stdin.readline())

  m = int(C / 60)
  C %= 60
  B += m

  h = int(B / 60)
  B %= 60
  A += h

  if 24 <= A:
    A %= 24

  print(str(int(A)) + " " + str(B) + " " + str(C))


if __name__ == "__main__":
    main()
