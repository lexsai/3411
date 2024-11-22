from fractions import Fraction

from huff import HuffmanTreeNode, generate_results, avg_len_from_results

def main():
  radix = 3
  input_values = [
    (1, Fraction(4, 10)),
    (2, Fraction(2, 10)),
    (3, Fraction(2, 10)),
    (4, Fraction(1, 10)),
    (5, Fraction(1, 10)),
  ]

  input_values = sorted(input_values, key=lambda x: (x[1], -x[0]), reverse=True)

  nodes = []
  for symbol, probability in input_values:
    nodes.append(HuffmanTreeNode(symbol, probability, radix))
  
  while len(nodes) % (radix - 1) != 1 and radix - 1 != 1:
    nodes.append(HuffmanTreeNode("dummy", 0, radix))

  for node in nodes:
    print(node.s, node.p)
  print('-')

  results = generate_results(nodes, radix)

  for code, symbol, p in results:
    print(f"s_{symbol} of probability {p} has code '{code}'")

  print("the average length of a codeword is", avg_len_from_results(results))

if __name__ == "__main__":
  main()
