from sys import stdin


def isRight(nums: list) -> bool:
  bRv: bool = False

  if nums[0] * nums[0] + nums[1] * nums[1] == nums[2] * nums[2]:
    bRv = True

  return bRv


def main():
  while True:
    n = list(map(int, stdin.readline().strip().split()))
    if n[0] == 0 and n[1] == 0 and n[2] == 0:
      break

    n.sort()
    if isRight(n) == True:
      print("right")
    else:
      print("wrong")


if __name__ == "__main__":
    main()
