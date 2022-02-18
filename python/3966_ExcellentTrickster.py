from sys import stdin


def getNormalNumber(n, k):
  sReturn = list()

  while n:
    sReturn.insert(0, n % k)
    n //= k

  return sReturn

# def getMinusNumber(n, k):
#   sReturn = ''

#   while k <= abs(n):
#     sReturn += str(n % k)

#     if n < 0:
#       n = n // k * -1
#     else:
#       n = int(n / k) * -1

#   n *= -1
#   if 0 < n:
#     n *= -1
#     sReturn += str(n % k)
#     n = int(n / k) - 1

#   sReturn += str(n * -1)

#   return sReturn[::-1]


def main():
  n, k = map(int, stdin.readline().split())
  
  # print(getNormalNumber(n, k))
  
  
  sReturn = list()

  while n:
    sReturn.insert(0, n % (k*k))
    n //= k*k

  count = 0
  f = 0

  for i in sReturn:
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

  # for i in range(n + 1):
  #   normal = getNormalNumber(i, k*k)
  #   # print(normal)
  #   if len(normal) < 2:
  #     # print(normal)
  #     count += 1
  #     continue
  #   elif len(normal) % 2 == 0:
  #     continue
  #   else:
  #     if normal[1] == 0:
  #       count += 1

  # print(count)


if __name__ == "__main__":
    main()
