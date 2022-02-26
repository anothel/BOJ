from sys import stdin
from collections import Counter


def main():
  N = int(stdin.readline().rstrip())
  nums: list = list()
  for _ in range(N):
    nums.append(int(stdin.readline().rstrip()))

  nums.sort()

  print(round(sum(nums)/N))
  # print("".join(str(int(statistics.mean(nums)))))
  print(nums[N//2])
  # print("".join(str(statistics.median(nums))))

  counts: list = Counter(nums).most_common(2)
  if len(counts) == 1:
    print(counts[0][0])
  else:
    if counts[0][1] == counts[1][1]:
      print(counts[1][0])
    else:
      print(counts[0][0])

  print("".join(str(nums[-1] - nums[0])))


if __name__ == "__main__":
    main()
