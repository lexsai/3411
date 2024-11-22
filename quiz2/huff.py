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

def generate_results(nodes, radix):
  while len(nodes) != 1:
    sample = nodes[-radix:]

    new_node = HuffmanTreeNode(float('inf'), sum([x.p for x in sample]), radix)
    for i, sample_node in enumerate(sample):
      new_node.setChild(radix - i - 1, sample_node)
      nodes.remove(sample_node)
    
    nodes.append(new_node)
    nodes = sorted(nodes, key=lambda n: (n.p, n.s), reverse=True)
    for node in nodes:
      print(node.s, node.p)
    print('-')

  results = nodes[0].get_results()
  return results

def avg_len_from_results(results):
  return sum([len(r[0])*r[2] for r in results])