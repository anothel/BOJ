from sys import stdin, stdout


def solve():
  a: int = 0
  b: int = 0
  s: int = 0
  count: int = 1
  r: bool = True
  for _ in range(int(stdin.readline().strip())):
    a, b, s = map(int, stdin.readline().strip().split())
    count = (count / a) * b
    r = not r if s == 1 else r
  stdout.write("0 " if r == True else "1 ")
  stdout.write("%d" % count)


if __name__ == "__main__":
    solve()
