from sys import stdin, stdout


def main():
  s = list(stdin.readline().strip())
  if s[-2] == str(1) and s[-1] == str(0):
    s.pop()
    s.pop()
    sum: int = 0
    i: int = 0
    while len(s) > 0:
      sum += int(s.pop()) * (10**i)
      i += 1
    print(sum + 10)
  else:
    tmp: int = int(s.pop())
    sum: int = 0
    i: int = 0
    while len(s) > 0:
      sum += int(s.pop()) * (10**i)
      i += 1
    print(sum + tmp)


if __name__ == "__main__":
    main()
