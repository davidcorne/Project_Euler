// Written by: DGC

#include <time.h>
#include <iostream>

int main(void) {
  clock_t t_start = clock();
  std::cout << "RUNNING PROBLEM XXX" << std::endl;

  std::cout << "run time: " << (clock() - t_start)/CLOCKS_PER_SEC
            << " seconds " << (clock() - t_start) << " microseconds"
            << std::endl;
  return 0;
}
