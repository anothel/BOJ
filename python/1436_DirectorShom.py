from sys import stdin


def main():
  N = int(stdin.readline().strip())

  i: int = 0
  nums: list = list()
  while True:
    i += 1
    if str(i).count("666"):
      nums.append(i)
    if N <= len(nums):
      break;
  print(i)


if __name__ == "__main__":
    main()
