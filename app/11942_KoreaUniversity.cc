#include <iostream>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::cout << "고려대학교";

  return 0;
}
