from sys import stdin, stdout


def main():
  n = int(stdin.readline().rstrip())
  if n == 1:
    stdout.write(str(1))
    return
  elif n % 2 != 0:
    stdout.write(str(0))
    return

  i: int = 1
  while i < n:
    i *= 2
    if i == n:
      stdout.write(str(1))
      return
  stdout.write(str(0))


if __name__ == "__main__":
  main()
