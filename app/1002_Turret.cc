#include <cmath>
#include <iostream>
#include <vector>

static int nTestCase(0);
static int X1(0), Y1(0), R1(0), X2(0), Y2(0), R2(0);
static int i(0);
static float add(0.0), sub(0.0), d(0.0);

class Point {
 public:
  Point(int x, int y, int r) : _x(x), _y(y), _r(r) {}

  int get_x() const { return _x; }
  int get_y() const { return _y; }
  int get_r() const { return _r; }

  void set_x(int x) { _x = x; }
  void set_y(int y) { _y = y; }
  void set_r(int r) { _r = r; }

 private:
  int _x;
  int _y;
  int _r;
};

static std::vector<std::pair<Point, Point>> vPoints;

float getDistance(const int& x1, const int& y1, const int& x2, const int& y2) {
  return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

float getDistance(const Point& p1, const Point& p2) {
  return getDistance(p1.get_x(), p1.get_y(), p2.get_x(), p2.get_y());
}

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::cin >> nTestCase;
  for (i = 0; i < nTestCase; i++) {
    std::cin >> X1 >> Y1 >> R1 >> X2 >> Y2 >> R2;
    vPoints.push_back(std::make_pair(Point(X1, Y1, R1), Point(X2, Y2, R2)));
  }

  for (auto x : vPoints) {
    add = abs(x.first.get_r() + x.second.get_r());
    sub = abs(x.first.get_r() - x.second.get_r());
    d = getDistance(x.first, x.second);

    if (sub < d && d < add) {
      std::cout << "2\n";
    } else if (add == d) {
      std::cout << "1\n";
    } else if (sub == d && d != 0) {
      std::cout << "1\n";
    } else if (d == 0 && x.first.get_r() == x.second.get_r()) {
      std::cout << "-1\n";
    } else if (add < d || d < sub || d == 0) {
      std::cout << "0\n";
    } else {
      exit(1);
    }
  }

  return 0;
}
