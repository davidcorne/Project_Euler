#include <math.h>
#include <iostream>
using namespace std;
int main() {
  cout << "RUNNING PROBLEM 4" << endl;
  
  for (int i = 1;i<1000;++i) {
    for (int j = 1;j<1000;++j) {
      int k = i*j;
      if (100000 < k) {
        int first_three = k / 1000;
        int last_three = k % 1000;
        if (first_three / 100 == last_three % 100) {
          int middle_first_two = first_three % 100;
          int middle_last_two = last_three / 10;
          if (middle_first_two / 10 == middle_last_two % 10) {
            cout << k << endl;
          }
        }
      }
    }
  }
  return 0;
}
