from sys import stdin


def fibo(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1

  return fibo(n-1) + fibo(n-2)


def main():

  print(fibo(int(stdin.readline().strip())))


if __name__ == "__main__":
    main()
