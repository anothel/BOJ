import sys


def main():
  A, B = map(int, input().split())
  B += int(sys.stdin.readline())

  h = B / 60
  B %= 60

  if 1 <= h:
    A += h
    if 24 <= A:
      A -= 24
  print(str(int(A)) + " " + str(B))


if __name__ == "__main__":
    main()
