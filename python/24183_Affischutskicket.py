from sys import stdin, stdout


def main():
  c4, a3, a4 = map(int, stdin.readline().strip().split())

  stdout.write(str("{:.6f}".format((0.229 * 0.324 * 2 * c4) +
               (0.297 * 0.42 * 2 * a3) + (0.21 * 0.297 * a4))))


if __name__ == "__main__":
    main()
