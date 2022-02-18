from sys import stdin


# K 진법으로 변환
def getNormalNumber(n, k):
  k_based_n = list()

  while n:
    k_based_n.insert(0, n % k)
    n //= k

  return k_based_n


# -K 진법으로 변환
def getMinusNumber(n, k):
  k_based_n = list()

  while k <= abs(n):
    k_based_n.insert(0, n % k)
    n //= k
    n *= -1

  n *= -1
  if 0 < n:
    n *= -1
    k_based_n.insert(0, n % k)
    n //= k

  k_based_n.insert(0, -n)

  return k_based_n


def main():
  n, k = map(int, stdin.readline().split())

  # for i in range(n + 1):
  #   print("i: " + str(i) + ", normal" + str(getNormalNumber(i, k)))
  # for i in range(n + 1):
  #   print("i: " + str(i) + ", minus" + str(getMinusNumber(i, k)))

  print(getNormalNumber(n, k*k))

  count = 0
  f = 0

  for i in getNormalNumber(n, k*k):
    if f == 0:
      if k <= i:
        count += k
        f = 1
      else:
        count += i
    count *= k

  count //= k
  if(f == 0):
    count += 1

  print(count)


if __name__ == "__main__":
    main()
