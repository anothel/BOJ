from sys import stdin, stdout


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)


def main():
  n: int = int(stdin.readline().strip())
  nums: list = list(map(int, stdin.readline().strip().split()))

  nGcd: int = gcd(nums[0], gcd(nums[1], nums[-1]))
  for i in range(1, nGcd//2+1):
    if nGcd % i == 0:
      stdout.write(str(i) + "\n")

  stdout.write(str(nGcd))


if __name__ == "__main__":
    main()
