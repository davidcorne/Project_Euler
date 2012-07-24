#include <math.h>
#include <iostream>
using namespace std;
int main() {
  cout << "RUNNING PROBLEM 2" << endl;
   int running_sum = 0;
   int previous = 0;
   int latest = 1;
   while (latest < 4000000) {
     // work out the fibonacci number confusingly
     latest = previous + latest;
     previous = latest - previous;
     if (latest % 2 == 0) {
       running_sum += latest;
     }
   }
   cout << " Sum of even fibonacci numbers less than 4,000,000 is "
        << running_sum << endl;
  
  return 0;
}
