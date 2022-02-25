from sys import stdin


def main():
  N, M = map(int, stdin.readline().strip().split())
  nums: list = list(map(int, stdin.readline().strip().split()))

  printValue: int = 0

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      for k in range(j + 1, len(nums)):
        v: int = nums[i] + nums[j] + nums[k]
        if v <= M and M - v < M - printValue:
          printValue = v
        if printValue == M:
          break
      if printValue == M:
        break
    if printValue == M:
      break
        

  print(printValue)


if __name__ == "__main__":
    main()
