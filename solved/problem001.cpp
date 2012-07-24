#include <math.h>
#include <iostream>
using namespace std;
int main() {
  cout << "RUNNING PROBLEM 1" << endl;
  int running_sum = 0;
  for (int i=1;i<1000;++i) {
    if ((i % 3) == 0 || (i % 5) == 0) {
      running_sum += i;
    }
  }
  cout << " Sum of multiples of 3 or 5 less than 1000 is "
       << running_sum << endl;
  return 0;
}
