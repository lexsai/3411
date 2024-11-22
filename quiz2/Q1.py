def permutate(C):
  P = []
  for i in range(1, len(C) + 1):
    for j in range(len(C) ** i):
      C_i = [ (j // len(C)**k) % len(C) for k in range(i) ]
      s = "".join([ C[k] for k in C_i ])
      P.append(s)
  return P

def has_duplicates(C):
  d = {}
  for c in C:
    if c in d:
      return c
    else:
      d[c] = True
  return False

def q1(C, possible_c_4):
  print("-" * 6, "q1", "-" * 6)
  for c_4 in possible_c_4:
    if x := has_duplicates(permutate(C + [c_4])):
      print(c_4, "has duplicates", x)
    else:
      print(c_4, "has no duplicates")

q1(
[ "1", "01", "001" ],
[
"1000",
"000",
"0001",
"0000"
])
