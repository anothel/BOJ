from sys import stdin


def main():
  nums: list = list()
  for _ in range(int(stdin.readline().strip())):
    nums.append(int(stdin.readline().strip()))

  nums.sort()

  for i in nums:
    print(i)


if __name__ == "__main__":
    main()
