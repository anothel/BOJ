from sys import stdin, stdout


def main():
  x1, y1, z1 = map(int, stdin.readline().strip().split())
  x2, y2, z2 = map(int, stdin.readline().strip().split())

  if x1 <= x2 and y1 <= y2 and z1 <= z2:
    stdout.write(str("A"))
  elif y1 <= y2 and z1 <= z2:
    if x1/2 <= x2 and y1/2 <= y2 and z1/2 <= z2:
      stdout.write(str("B"))
    else:
      stdout.write(str("C"))
  elif z1 <= z2:
    if y1/2 <= y2 and z1/2 <= z2:
      stdout.write(str("D"))
    else:
      stdout.write(str("E"))
  else:
    stdout.write(str("E"))


if __name__ == "__main__":
    main()
