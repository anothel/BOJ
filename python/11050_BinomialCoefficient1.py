from sys import stdin


def fac(n: int) -> int:
  nReturnValue: int = 1

  for i in range(1, n + 1):
    nReturnValue *= i

  return nReturnValue


def main():
  N, K = map(int, stdin.readline().strip().split())
  print(fac(N) // (fac(K) * fac(N-K)))


if __name__ == "__main__":
    main()
