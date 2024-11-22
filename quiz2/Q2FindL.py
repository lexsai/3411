"""
A radix 4 instantaneous code (I-code) has codeword lengths 
(not necessarily in order) 2,2,2,3,ℓ and Kraft-McMillan coefficient K=1764.

What is the value of ℓ?
"""

import math
from fractions import Fraction

def main():
  radix = 4
  k = Fraction(5, 8)
  known=[1,1,2]

  for x in known:
    k -= Fraction(1, radix) ** x

  print(math.log(k)/math.log(Fraction(1, radix)))

if __name__ == "__main__":
  main()
