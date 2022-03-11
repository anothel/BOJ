from sys import stdin, stdout


def main():
  wc, hc, ws, hs = map(int,stdin.readline().rstrip().split())
  stdout.write(str(1 if ws + 1 < wc and hs + 1 < hc else 0))


if __name__ == "__main__":
  main()
