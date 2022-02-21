from sys import stdin


def main():
  remainder_list = list()
  for _ in range(10):
    remainder_list.append(int(stdin.readline().strip()) % 42)
  print(len(list(set(remainder_list))))


if __name__ == "__main__":
    main()
