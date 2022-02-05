#include <iostream>

static int A = 0, B = 0;

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::cin >> A >> B;

  std::cout << A / B << ".";

  A = A % B;
  for (int i = 0; i < 1000; i++) {
    A *= 10;
    int a = A / B;
    if(0 < a) std::cout << a;
    else break;
    A = A - (A / B) * B;
  }

  return 0;
}