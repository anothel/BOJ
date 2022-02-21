from sys import stdin


def main():
  v_list = list()

  v = int(stdin.readline().strip())
  if v < 10:
    v_list.append(0)
    v_list.append(v)
  else:
    v_list.append(v//10)
    v_list.append(v % 10)

  value = v
  first = v_list[0]
  second = v_list[1]
  count = 0

  while 1:
    count += 1
    value = ((value % 10) * 10) + ((first + second) % 10)

    first = value // 10
    second = value % 10

    if value == v:
      print(count)
      break


if __name__ == "__main__":
    main()
