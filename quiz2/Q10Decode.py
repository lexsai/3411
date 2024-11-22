from decimal import *

def main():
  getcontext().prec = 100

  encoded_message = Decimal(0.8876)

  symbols = [
    ("s1", Decimal(0.8)),
    ("s2", Decimal(0.1)),
    ("*", Decimal(0.1)),
  ]

  start = Decimal(0)
  width = Decimal(1)

  decoded_message = ""
  while decoded_message == "" or decoded_message[-1] != "*":
    for i, (s, p) in enumerate(symbols):
      section_start = start + sum([x[1] for x in symbols[:i]]) * width
      section_end = section_start + p * width
      print(section_start, section_end, s)
      if encoded_message >= section_start and encoded_message < section_end:
        print(encoded_message, "was in", section_start, "and", section_end) 
        decoded_message += s
        width *= p
        start = section_start
        break
  
  print(decoded_message)

if __name__ == "__main__":
  main()
