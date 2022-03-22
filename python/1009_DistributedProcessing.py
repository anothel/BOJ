from sys import stdin, stdout


def getNums(a: int, nums: list):
  x: int = a
  y: int = a

  nums.append(a if a != 0 else 10)

  while True:
    x *= a
    x %= 10
    if x == y:
      break
    nums.append(x)


def main():
  for _ in range(int(stdin.readline().strip())):
    a, b = map(int, stdin.readline().strip().split())

    nums: list = list()
    getNums(a % 10, nums)

    stdout.write(str(nums[b % len(nums) - 1 if b % len(nums) != 0 else len(nums) - 1]
                 if len(nums) != 1 else nums[0]) + "\n")


if __name__ == "__main__":
    main()
