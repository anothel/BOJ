from sys import stdin, stdout


def main():
  dp: list = list()

  for _ in range(int(stdin.readline().strip())):
    dp.append(list(map(int, stdin.readline().strip().split())))

  for i in range(1, len(dp)):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][1], dp[i-1][0])

  stdout.write(str(min(dp[-1])))


if __name__ == "__main__":
    main()
