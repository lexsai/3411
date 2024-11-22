from fractions import Fraction

from huff import HuffmanTreeNode, generate_results, avg_len_from_results

class HuffmanTreeNode:
  def __init__(self, s, p, radix):
    self.s = s
    self.p = p
    self.radix = radix

    self.children = [None] * radix

  def get_results(self):
    results = []
    self.rec_get_results(results, "")
    return sorted(results, key=lambda x: (x[2], -x[1]), reverse=True)

  def rec_get_results(self, results, code):
    children = [x for x in self.children if x != None]

    if len(children) == 0:
      if self.s != 'dummy':
        results.append((code, self.s, self.p))
      return

    for i, child in enumerate(children):
      child.rec_get_results(results, code + str(self.radix - 1 - i))

  def setChild(self, index, value):
    if index > self.radix:
      raise IndexError
    
    self.children[index] = value

def main():
  radix = 3
  input_values = [
    (1, Fraction(3, 5)),
    (2, Fraction(2, 5)),
  ]

  ext_input_values = []

  symbol_dict = {}

  j = 1
  for x in input_values:
    for y in input_values:
      ext_input_values.append((j, x[1] * y[1]))
      symbol_dict[j] = (x[0], y[0])
      j += 1

  ext_input_values = sorted(ext_input_values, key=lambda x: (x[1], x[0]), reverse=True)

  nodes = []
  for symbol, probability in ext_input_values:
    nodes.append(HuffmanTreeNode(symbol, probability, radix))

  while len(nodes) % (radix - 1) != 1 and radix - 1 != 1:
    nodes.append(HuffmanTreeNode("dummy", 0, radix))

  for node in nodes:
    print(node.s, node.p)
  print('-')

  results = generate_results(nodes, radix)
  
  for code, symbol, p in results:
    print(f"s_{symbol_dict[symbol]} of probability {p} has code '{code}'")

  print("the average length of a codeword is", avg_len_from_results(results))

  print("!!!!!!!!CHECK WHETHER ITS 'PER ORIGINAL SYMBOL', DIVIDE BY EXTENSION IF SO!!!!!!!!")

if __name__ == "__main__":
  main()
