from sys import stdin, stdout


def in_cache(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper


@in_cache
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1


def main():
  for T in range(int(stdin.readline().strip())):
    N, M = map(int, stdin.readline().strip().split())
    stdout.write(str(factorial_recursive(M) //
                 (factorial_recursive(N) * factorial_recursive(M-N))) + "\n")


if __name__ == "__main__":
    main()
