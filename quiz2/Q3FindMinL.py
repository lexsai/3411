from fractions import Fraction

def main():
  radix = 2
  known = [1,2,3,4,6,7]

  for l in range(100):
    x = 0
    for y in known:
      x += Fraction(1, radix) ** y

    x += Fraction(1, radix) ** l
    if x <= 1:
      print(l)
      break

if __name__ == "__main__":
  main()
