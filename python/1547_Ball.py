from sys import stdin, stdout


def main():
  ball:int = 1
  for _ in range(int(stdin.readline().strip())):
    a, b = map(int, stdin.readline().strip().split())
    if a == ball:
      ball = b
    elif b == ball:
      ball = a
  stdout.write(str(ball))
    


if __name__ == "__main__":
    main()
