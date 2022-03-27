from sys import stdin, stdout


# def binary(tar: int, l: list) -> bool:
#   start: int = 0
#   end: int = len(l) - 1
#   mid: int = (start + end) // 2

#   while end-start >= 0:
#     if l[mid] == tar:
#       return True
#     elif l[mid] <= tar:
#       start = mid + 1
#     else:
#       end = mid - 1
#     mid = (end + start) // 2

#   return False

def binary(l: list, tar: int, low: int, high: int) -> bool:
  if low > high:
    return False

  mid: int = (low + high) // 2
  if l[mid] == tar:
    return True
  elif l[mid] <= tar:
    return binary(l, tar, mid+1, high)
  else:
    return binary(l, tar, low, mid-1)


def main():
  n: int = int(stdin.readline().strip())
  finders: list = sorted(map(int, stdin.readline().strip().split()))

  m: int = int(stdin.readline().strip())
  for i in list(map(int, stdin.readline().strip().split())):
    # stdout.write(str(1 if binary(i, finders) else 0) + str("\n"))
    stdout.write(
        str(1 if binary(finders, i, 0, len(finders)-1) else 0) + str("\n"))


if __name__ == "__main__":
    main()
