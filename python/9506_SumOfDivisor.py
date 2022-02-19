from sys import stdin


def getDivisor(n, d_list):
  for i in range(n):
    if i == 0:
      continue
    if n % i == 0:
      d_list.append(i)

  return d_list


def getSentence(d_list):
  s = ''

  for i in range(len(d_list)):
    if i == 0:
      s = str(d_list[0])
    else:
      s += ' + ' + str(d_list[i])

  return s


def getSum(n, divisor_list):
  sum = 0

  for i in range(len(getDivisor(n, divisor_list))):
    sum += divisor_list[i]

  return sum


def doExecute(n, divisor_list):
  if n == getSum(n, divisor_list):
    print(str(n) + ' = ' + getSentence(divisor_list))
  else:
    print(str(n) + " is NOT perfect.")


def main():
  while 1:
    divisor_list = list()
    n = int(stdin.readline())
    if n == -1:
      break

    doExecute(n, divisor_list)


if __name__ == "__main__":
    main()
