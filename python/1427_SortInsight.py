from sys import stdin


def main():
  for s in sorted(list(map(int, stdin.readline().strip())), reverse=True):
    print("", end="".join(str(s)))


if __name__ == "__main__":
    main()
