#include <iostream>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::cout << "SHIP NAME      CLASS          DEPLOYMENT IN SERVICE\n";
  std::cout << "N2 Bomber      Heavy Fighter  Limited    21        \n";
  std::cout << "J-Type 327     Light Combat   Unlimited  1         \n";
  std::cout << "NX Cruiser     Medium Fighter Limited    18        \n";
  std::cout << "N1 Starfighter Medium Fighter Unlimited  25        \n";
  std::cout << "Royal Cruiser  Light Combat   Limited    4         \n";
  return 0;
}
