from sys import stdin


def main():
  for T in range(int(stdin.readline().strip())):
    k = int(stdin.readline().strip())
    n = int(stdin.readline().strip())

    f: list = [i for i in range(1, n+1)]
    for _ in range(k):
      for j in range(1, n):
        f[j] += f[j-1]
    print(f[-1])


if __name__ == "__main__":
    main()
