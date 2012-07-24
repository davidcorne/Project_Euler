#include <math.h>
#include <iostream>
using namespace std;
int main() {
  cout << "RUNNING PROBLEM 9" << endl;
  // finding a^2 + b^2 = c^2 s.t a + b + c = 1000
  int a_1 = -1;
  int b_1 = -1;
  int c_1 = -1;
  for (int a=1;a<1000;++a) {
    for (int b=1;b<1000;++b) {
      int c = ((1000-a) - b);
      if ((a*a + b*b) == c*c) {
        a_1 = a;
        b_1 = b;
        c_1 = c;
        break;
      }
    }
  }
  cout << a_1 << " , " << b_1 << " , " << c_1 << " and "
       << a_1 + b_1 + c_1 << " then " << a_1*b_1*c_1 << endl; 
  
  return 0;
}
