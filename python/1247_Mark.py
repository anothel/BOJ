from sys import stdin, stdout


def main():
  for _ in range(3):
    sum: int = 0
    for _ in range(int(stdin.readline().strip())):
      sum += int(stdin.readline().strip())
    if sum == 0:
      stdout.write(str("0 \n"))
    elif sum > 0:
      stdout.write(str("+ \n"))
    elif sum < 0:
      stdout.write(str("- \n"))


if __name__ == "__main__":
    main()
