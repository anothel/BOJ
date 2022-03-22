from sys import stdin, stdout


def main():
  a3 = int(stdin.readline())
  a2 = int(stdin.readline())
  a1 = int(stdin.readline())
  b3 = int(stdin.readline())
  b2 = int(stdin.readline())
  b1 = int(stdin.readline())

  if a3 * 3 + a2 * 2 + a1 * 1 > b3 * 3 + b2 * 2 + b1:
    stdout.write(str("A"))
  elif a3 * 3 + a2 * 2 + a1 * 1 < b3 * 3 + b2 * 2 + b1:
    stdout.write(str("B"))
  else:
    stdout.write(str("T"))


if __name__ == "__main__":
    main()
