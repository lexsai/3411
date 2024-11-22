from fractions import Fraction

def main():
  input_values = [1,1,2,2,3,3,4,4]

  for r in range(1, 100):
    x = 0
    for val in input_values:
      x += (Fraction(1, r)) ** val
    
    if x <= 1:
      print("radix", r)
      break

if __name__ == "__main__":
  main()
