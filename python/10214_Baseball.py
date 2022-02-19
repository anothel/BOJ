from sys import stdin


def main():
  for T in range(int(stdin.readline())):
    score_y = 0
    score_k = 0
    for i in range(9):
      Y, K = map(int, stdin.readline().split())
      score_y += Y
      score_k += K
    if score_y < score_k:
      print('Korea')
    elif score_k < score_y:
      print('Yonsei')
    else:
      print('Draw')


if __name__ == "__main__":
    main()
