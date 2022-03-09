#include <iostream>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  int A = 0, B = 0;
  std::cin >> A >> B;

  std::cout << B + B - A << "\n";

  return 0;
}
