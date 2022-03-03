#include <iostream>
#include <string>
#include <vector>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::string sNumber = "";
  std::cin >> sNumber;
  std::cout << (int)std::stol(sNumber, NULL, 16) << "\n";

  return 0;
}
