from sys import stdin, stdout


def main():
  C: int = int(stdin.readline().strip())
  nums: list = list(map(int, stdin.readline().strip().split()))

  stdout.write(str(max(nums) * min(nums)) + "\n")


if __name__ == "__main__":
    main()
