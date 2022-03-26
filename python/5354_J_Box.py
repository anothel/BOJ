from sys import stdin, stdout


def prinT(n: int):
  for i in range(n):
    for j in range(n):
      if i == 0 or i == n -1:
        stdout.write(str("#"))
        continue
      if j == 0 or j == n -1:
        stdout.write(str("#"))
      else:
        stdout.write(str("J"))
    stdout.write(str("\n"))
  stdout.write(str("\n"))


def main():
  for _ in range(int(stdin.readline().rstrip())):
    prinT(int(stdin.readline().rstrip()))


if __name__ == "__main__":
  main()
