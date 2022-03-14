from sys import stdin, stdout


def main():
  x, y = map(int, stdin.readline().strip().split())

  if (x+y) % 2 != 0 or x < y:
    stdout.write(str(-1))
  else:
    stdout.write(str((x + y) // 2) + " " +
                 str(abs(x - ((x + y) // 2))))


if __name__ == "__main__":
    main()
