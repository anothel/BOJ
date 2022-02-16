import sys


def main():
  count = sys.stdin.readline()
  for i in range(int(count)):
    A, B = map(int, input().split())
    print("Case #" + str(i + 1) + ": " + str(A) +
          " + " + str(B) + " = " + str(A + B))


if __name__ == "__main__":
    main()
