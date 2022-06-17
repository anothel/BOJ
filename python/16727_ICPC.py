from sys import stdin, stdout


def main():
  p1, e1 = map(int, stdin.readline().strip().split())
  e2, p2 = map(int, stdin.readline().strip().split())

  if (p1 + p2) > (e1 + e2):
    stdout.write(str("Persepolis"))
  elif (e1 + e2) > (p1 + p2):
    stdout.write(str("Esteghlal"))
  else:
    if p2 > e1:
      stdout.write(str("Persepolis"))
    elif e1 > p2:
      stdout.write(str("Esteghlal"))
    else:
      stdout.write(str("Penalty"))


if __name__ == "__main__":
    main()
