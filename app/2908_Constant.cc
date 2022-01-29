#include <algorithm>
#include <iostream>
#include <string>

static int x, y = 0;

int comp(const std::string &rhs1, const std::string &rhs2) {
  return std::stoi(rhs1) < std::stoi(rhs2) ? std::stoi(rhs2) : std::stoi(rhs1);
}

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::cin >> x >> y;

  std::string x_string(std::to_string(x)), y_string(std::to_string(y));

  std::reverse(std::begin(x_string), std::end(x_string));
  std::reverse(std::begin(y_string), std::end(y_string));

  std::cout << comp(x_string, y_string) << "\n";

  return 0;
}
