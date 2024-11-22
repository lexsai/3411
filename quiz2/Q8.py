from fractions import Fraction

from huff import HuffmanTreeNode, generate_results, avg_len_from_results

def main():
  radix = 2

  t_matrix = [
    [Fraction(7, 10), Fraction(1, 10), Fraction(1, 5)],
    [Fraction(1, 5), Fraction(3, 5), Fraction(4, 10)],
    [Fraction(1, 10), Fraction(3, 10), Fraction(1, 2)],
  ]
  eq_vector = [
    Fraction(4, 16),
    Fraction(7, 16),
    Fraction(5, 16)
  ]
  
  dim = len(t_matrix)
  assert len(t_matrix[0]) == dim

  avg_lengths = []

  for i in range(dim):
    nodes = []

    probabilities = []
    for j in range(dim):
      probabilities.append(t_matrix[j][i])

    for s, p in enumerate(sorted(probabilities, reverse=True)):
      nodes.append(HuffmanTreeNode(s + 1, p, radix))
        
    if len(nodes) % (radix - 1) == 0 and radix - 1 != 1:
      nodes.append(HuffmanTreeNode("dummy", 0, radix))

    for node in nodes:
      print(node.s, node.p)
    print('-')

    results = generate_results(nodes, radix)
    print(results)
    avg_len = avg_len_from_results(results)
    
    print("abcd", results, avg_len)

    avg_lengths.append(avg_len)

  avg_codeword_len = 0
  print(avg_lengths)
  for i in range(dim):
    avg_codeword_len += avg_lengths[i] * eq_vector[i]

  print(avg_codeword_len)

if __name__ == "__main__":
  main()
