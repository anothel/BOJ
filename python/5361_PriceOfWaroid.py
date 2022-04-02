from sys import stdin, stdout


def main():
  prices: list = [350.34, 230.90, 190.55, 125.30, 180.90]
  for _ in range(int(stdin.readline().rstrip())):
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    price: float = 0.0
    for i in range(5):
      price += nums[i] * prices[i]
    stdout.write(str("$%.2f\n" % price))


if __name__ == "__main__":
    main()
