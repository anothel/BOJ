from sys import stdin, stdout


def calcT(nInput:int) -> int:
  nRv:int = 0
  for i in range(1, nInput + 1):
    nRv += i
    
  return nRv

def solve():
  for _ in range(int(stdin.readline().strip())):
    nRv :int = 0
    for k in range(1, int(stdin.readline().strip())+1):
      nRv += k * calcT(k+1)
    stdout.write("%d\n" % nRv)


if __name__ == "__main__":
    solve()
