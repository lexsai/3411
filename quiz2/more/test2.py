from math3411 import *
from fractions import Fraction

def q1(C, possible_c_4):
  print("-" * 6, "q1", "-" * 6)
  for c_4 in possible_c_4:
    if has_duplicates(permutate(C + [c_4])):
      print(c_4, "has duplicates")

def q2_find_l(r, l, K):
  print("-" * 6, "q2_find_l", "-" * 6)
  l = [ int(l_i) for l_i in l ]
  for i in range(1, 10):
    if abs(K - kraft_mcmillan(r, l + [i])) < 0.0001:
      print("l =", i)
      break

def q2_find_c(r, l):
  print("-" * 6, "q2_find_c", "-" * 6)
  l = [ int(l_i) for l_i in l ]
  
  last = 0
  l_j = 0
  
  c = {}
  
  for l_i in l:
    if l_i != l_j:
      last *= r**(l_i - l_j)
      l_j = l_i
    if l_i not in c:
      c[l_i] = []
    c[l_i].append(num_to_code(last, r))
    last += 1
  
  for l_i, c_i in c.items():
    for x in c_i:
      X = [str(y) for y in [0] * (l_i - len(x)) + x[::-1]]
      print(l_i, "-", "".join(X))

def q3_min_radix(l):
  print("-" * 6, "q3_min_radix", "-" * 6)
  l = [ int(l_i) for l_i in l ]
  for r in range(1, 10):
    K = kraft_mcmillan(r, l)
    if K <= 1.0:
      print("r =", r, "| K =", K)
      break

def q3_min_l(l, r):
  print("-" * 6, "q3_min_l", "-" * 6)
  l = [ int(l_i) for l_i in l ]
  for l_q in range(1, 10):
    K = kraft_mcmillan(r, l + [l_q])
    if K <= 1.0:
      print("l =", l_q, "| K =", K)
      break

def q4_average_length(p, r):
  print("-" * 6, "q4_average_length", "-" * 6)
  p = [ int(p_i) for p_i in p.split(",") ]
  print("average length =", huffman_average_length(p, r))

def q5_encode(s, n):
  print("-" * 6, "q5_encode", "-" * 6)
  c = [ comma_code(int(s_i), n) for s_i in s ]
  print("".join(c))

def q5_decode(s, n):
  print("-" * 6, "q5_decode", "-" * 6)
  d = []
  while len(s) > 0:
    for i in range(1, n + 2):
      if s.startswith(comma_code(i, n)):
        s = s[len(comma_code(i,n)):]
        d.append(i)
        break
  print("".join([ "s"+str(d_i) for d_i in d]))

def q7_average_length(p, denom, r, n, original=False):
  print("-" * 6, "q7_average_length", "-" * 6)
  q = [ int(p_i) for p_i in p ]
  p = []
  for i in range(len(q)**n):
    c_n = padded_num_to_code(i, len(q), n)
    p_n = prod([ q[c_i] for c_i in c_n ])
    p.append(p_n)
  
  p = [ int(p_i) for p_i in p ]
  avg_len = huffman_average_length(p, r)
  avg_len = Fraction(avg_len, denom ** n)
  if original:
    avg_len = Fraction(avg_len, n)
  print("average length =", avg_len.numerator, "/", avg_len.denominator)

def q7_encode(p, denom, r, n):
  print("-" * 6, "q7_encode", "-" * 6)
  q = [ int(p_i) for p_i in p ]
  p = []
  for i in range(len(q)**n):
    c_n = padded_num_to_code(i, len(q), n)
    p_n = prod([ q[c_i] for c_i in c_n ])
    p.append(p_n)
  
  pad = 0
  
  if r > 2:
    while len(p) % (r - 1) != 1:
      p += [0]
      pad += 1
  p = sorted(p, reverse=True)
  
  A = []
  E = []
  
  x = p.copy()
  y = p[:-r].copy()
  s = sum(p[-r:])
  highest = [ i for i in range(len(y)) if y[i] < s ][0]
  
  while True:
    E_i = []
    for i in range(highest):
      E_i.append(i)
    for i in range(highest, len(y)):
      E_i.append(i + 1)
    for i in range(len(y), len(y) + r):
      E_i.append(highest)
    E.append(E_i)
    
    y.insert(highest, s)
    x = y.copy()
    y = x[:-r].copy()
    s = sum(x[-r:])
    
    if len(x) == r:
      E.append([0] * r)
      break
    else:
      highest = [ i for i in range(len(y)) if y[i] < s ][0]
  
  x = []
  
  pos = len(p) - pad - 1
  for layer in E:
    if pos >= len(layer) - r:
      x.append(pos - (len(layer) - r))
    pos = layer[pos]
  
  print("".join([ str(c) for c in reversed(x) ]))

def q8_average_length(p, denom_p, h_1, h_2, h_3, denom_h):
  print("-" * 6, "q8_average_length", "-" * 6)

  a = Fraction(huffman_average_length(h_1, 2), denom_h)
  b = Fraction(huffman_average_length(h_2, 2), denom_h)
  c = Fraction(huffman_average_length(h_3, 2), denom_h)

  print(Fraction(p[0]*a + p[1]*b + p[2]*c, denom_p))

def q8_decode(h_E, m, h_1, h_2, h_3):
  print("-" * 6, "q8_decode", "-" * 6)
  idx = [ i for i in range(len(h_E)) if m.startswith(h_E[i]) ][0]
  x = h_E[idx]
  m = m[len(x):]
  
  h_n = [h_1, h_2, h_3]
  
  d = []
  d.append(idx)
  
  while len(m) > 0:
    # print(idx, h_n[idx], m)
    new_idx = [ i for i in range(len(h_n[idx])) if m.startswith(h_n[idx][i]) ][0]
    d.append(new_idx)
    x = h_n[idx][new_idx]
    m = m[len(x):]
    idx = new_idx
  
  print("".join(["s"+str(i+1) for i in d]))

def q8_encode(h_E, m, h_1, h_2, h_3):
  print("-" * 6, "q8_encode", "-" * 6)
  m = [ int(c) for c in m ]
  
  pos = m[0] - 1
  e = h_E[pos]
  
  print(f"H_e s{pos + 1}", h_E[pos])
  
  h_n = [h_1, h_2, h_3]
  
  for c in m[1:]:
    x = h_n[pos][c - 1]
    e += x
    print(f"H_{pos + 1} s{c}", x)
    pos = c - 1
  print(e)

def q9_decode(m):
  print("-" * 6, "q9_decode", "-" * 6)
  m = [ (int(c[0]), c[1]) for c in m.split(",") ]
  
  d = [""]
  
  for c in m:
    a, b = c
    d.append(d[a] + b)
  
  print("".join(d))

def q9_encode(m):
  print("-" * 6, "q9_encode", "-" * 6)
  d = [ "" ]
  l = 0
  e = []
  while len(m) > 0:
    idx = [ i for i in range(len(d) - 1, -1, -1) if m.startswith(d[i]) ][0]
    new = d[idx] + m[len(d[idx])]
    e.append((idx, new))
    d.append(new)
    m = m[len(d[idx])+1:]
  print(e)

def q10_decode(T, m):
  print("-" * 6, "q10_decode", "-" * 6)
  
  s = []
  
  u = 0.0
  v = 1.0
  
  T = [ (T[i], T[i + 1]) for i in range(len(T) - 1)]
  for X in range(4):
    for itvl, idx in zip(T, range(len(T))):
      a, b = itvl
      x = u + a * (v - u)
      y = u + b * (v - u)
      if m >= x and m < y:
        s_i = idx
        u = x
        v = y
        break
    if s_i is None:
      print("error", s, u, v, m)
    s.append(s_i)
    if s_i == len(T) - 1:
      break
  
  print("".join([ "s"+str(s_i+1) for s_i in s if s_i != len(T) - 1]) + "*")

def q10_encode(P, a, m):
  print("-" * 6, "q10_decode", "-" * 6)
  D = {}
  t = 0.0
  for a, b in zip(a, P):
    D[a] = (t, t + b)
    t += b
  s = 0.5
  for c in m[::-1]:
    x, y = D[c]
    s = x + s * (y - x)
  print(round(s, 5))

q1(
[ "10", "000", "100" ],
[
"11",
"1",
"01",
"101"
])

q2_find_l(2, "22235", 59/64)
q2_find_c(2, "123457")

q3_min_radix("1234567")
q3_min_l("223336", 2)

q4_average_length("7,2,2,2,2,1,1", 3)

q5_encode("52454", 4)
q5_decode("111101110101110", 4)

q7_average_length(
"61",7,
3,3,
original=False
)

q7_encode(
"21",3,
3,3
)

q8_decode(
  ["00","11","10"],
  "110110100",
  ["0","10","11"],
  ["01","1","00"],
  ["10","0","11"],
)

q8_encode(
  ["11","10","0"],
  "21322",
  ["01","1","00"],
  ["00","1","01"],
  ["00","01","1"],
)

q8_average_length(
  [12,47,61],
  120,
  [1,2,7],
  [1,3,6],
  [1,5,4],
  10
)

q9_decode("0a,1c,2c,3b,4a,4b")
q9_encode("caabaaabcabcc")

q10_encode([0.8, 0.1, 0.1], "ab*", "ab*")
q10_decode([0.0, 0.7, 0.8, 1.0], 0.3871)
