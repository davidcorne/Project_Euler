#!/utils/bin/perl -w

use bignum;
#600851475143 = 71x8462696833
#8462696833 = 839x10086647
#10086647 = 1471x6857
$huge_int = 10086647;
print $huge_int, "\n";
$iterator = 1;
while ($iterator < sqrt($huge_int)) {
  $temp = $huge_int % $iterator;
  if ($temp == 0) {
    print $iterator, "\n";
  }
  $iterator += 2;
}

print "DONE\n";
