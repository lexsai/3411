from decimal import *

def main():
  getcontext().prec = 10

  symbols = [
    ("a", Decimal(0.3)),
    ("b", Decimal(0.2)),
    ("stop", Decimal(0.5)),
  ]
  message = ["b","a","b","stop"]
  
  start = Decimal(0)
  width = Decimal(1)

  for char in message:
    i, (s, p) = next((i, x) for i, x in enumerate(symbols) if x[0] == char)
    section_start = sum([x[1] for x in symbols[:i]])

    start += section_start * width
    width *= p

    print(start, width)
  print('-')

  print("message is between", start, "to", start + width)
  print("one answer could be", start + width/2)

if __name__ == "__main__":
  main()
