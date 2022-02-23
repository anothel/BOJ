from sys import stdin


def checker(s: list, aList: list) -> int:
  rv: int = 1

  for i in range(len(s)):
    if 0 < i and s[i] == s[i - 1]:
      continue

    if aList[ord(s[i]) - ord('a')] == 0:
      aList[ord(s[i]) - ord('a')] = 1
    else:
      rv = 0
      break

  return rv


def main():
  sum: int = 0

  for _ in range(int(stdin.readline().strip())):
    sum += checker(list(stdin.readline().strip()),
                   [0 for _ in range(ord('a'), ord('z') + 1)])

  print(sum)


if __name__ == "__main__":
    main()
