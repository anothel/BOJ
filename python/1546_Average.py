from sys import stdin


def main():
  N = int(stdin.readline().strip())
  sub_list = list(map(int, stdin.readline().strip().split()))

  sum = 0
  for i in sub_list:
    sum += i / max(sub_list) * 100
    
  sum /= len(sub_list)
  
  print(sum)


if __name__ == "__main__":
    main()
