from sys import stdin, stdout


def main():
  nums: list = list(map(int, stdin.readline().rstrip().split()))

  if nums[0] + nums[1] == nums[2]:
    stdout.write(str("%d+%d=%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] - nums[1] == nums[2]:
    stdout.write(str("%d-%d=%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] * nums[1] == nums[2]:
    stdout.write(str("%d*%d=%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] / nums[1] == nums[2]:
    stdout.write(str("%d/%d=%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] == nums[1] + nums[2]:
    stdout.write(str("%d=%d+%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] == nums[1] - nums[2]:
    stdout.write(str("%d=%d-%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] == nums[1] * nums[2]:
    stdout.write(str("%d=%d*%d" % (nums[0], nums[1], nums[2])))
  elif nums[0] == nums[1] / nums[2]:
    stdout.write(str("%d=%d/%d" % (nums[0], nums[1], nums[2])))


if __name__ == "__main__":
    main()
