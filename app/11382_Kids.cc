#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  long long A = 0, B = 0, C = 0;
  std::cin >> A >> B >> C;

  std::cout << A + B + C;

  return 0;
}
