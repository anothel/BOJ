from sys import stdin


def main():
  N = int(stdin.readline())

  for i in range(N+1):
    if i < 2:
      continue

    while N % i == 0:
      print(i)
      N /= i


if __name__ == "__main__":
    main()
