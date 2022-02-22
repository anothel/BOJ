from sys import stdin


def main():
  ascending = list()
  for i in range(1, 9):
    ascending.append(i)
  descending = ascending.copy()
  descending.reverse()

  input = list(map(int, stdin.readline().strip().split()))

  if input == ascending:
    print("ascending")
  elif input == descending:
    print("descending")
  else:
    print("mixed")


if __name__ == "__main__":
    main()
