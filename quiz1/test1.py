from math3411 import *
from z3 import *
 
def H_y(H, y, P):
  H = H.strip().split('\n')
  v = []
  for i in range(len(H)):
    v.append(sum([int(H[i][j]) * int(y[j]) for j in range(len(H[0]))]) % P)
  return v
 
def solve_q1(A, k):
  A = [ 10 if x == 'X' else int(x) for x in A if x != '-' ]
  for i in range(11):
    A[k - 1] = i
    if ISBN(A) == 0:
      print(f"q1: correct digit is: {i}")
 
def solve_q2_encode(msg):
  mat = [ [ int(x) for x in bin(ord(row))[2:] ] for row in msg ]
  vec = []
 
  for i in range(len(mat[0])):
    vec.append(sum([ mat[j][i] for j in range(len(mat)) ]) % 2)
 
  check = chr(int(''.join(map(str, vec[1:])), 2))
 
  print("q2: encoded:", msg + check)
 
def solve_q2_correct(msg):
  msg = msg.split(' ')
 
  a = 0
  for row in msg:
    if sum([ int(x) for x in row ]) % 2 != 0:
      break
    a += 1
 
  b = 0
  for row in msg:
    b = int(row, 2) ^ b
 
  print(f"q2: error at {a * 8 + 8 - log(b) / log(2)}")
 
  m = [ int(x, 2) for x in msg ]
  m[a] ^= b
  print("q2: message:", ''.join([ chr(x & 127) for x in m ]))
 
def solve_q3_rref(H, P):
  H = H.strip()
  A = []
  for line in H.split('\n'):
    v = []
    for col in line:
      v.append(int(col))
    A.append(v)
  H = GFMatrix(P, A)
  H = H.row_echelon_form().reduced()
  print("q3")
  H.show()
 
def solve_q4_encode(H, P, check, msg):
  H = H.strip()
  A = []
  for line in H.split('\n'):
    v = []
    for col in line:
      v.append(int(col))
    A.append(v)
  H = GFMatrix(P, A)
  H = H.reduced()
 
  info = list(zip([ x for x in range(1,H.width()+1) if x not in check ], msg))
 
  X = [ Int(f"x{i + 1}") for i in range(H.width()) ]
 
  s = Solver()
  for x in X:
    s.add(x >= 0)
  for bit in info:
    pos, val = bit
    s.add(X[pos - 1] == val)
  for i in range(H.height()):
    s.add(sum([ X[j] * H.m[i][j] for j in range(H.width()) ]) % P == 0)
  s.check()
  sol = s.model()
  sol = sorted ([(d, sol[d]) for d in sol], key = lambda x: str(x[0]))
  sol = ''.join([ str(d[1].as_long() % P) for d in sol ])
  print("q4:", sol)
 
def solve_q5_mul(H, y, P):
  v = H_y(H,y,P)
  print("q5:", v)
 
def solve_q6_mul(P, H, G_list):
  for G in G_list:
    a, b = G
    v1 = H_y(H,a,P)
    v2 = H_y(H,b,P)
    print("q6:", v1, v2)

def solve_q7_weight(H, P):
  H = H.strip()
  A = []
  for line in H.split('\n'):
    v = []
    for col in line:
      v.append(int(col))
    A.append(v)
  k = len(A)
  
  w = lambda v : len([ x for x in v if x != 0 ]) 
  
  min_w = 9999
  
  for i in range(1,P ** k):
    l = [ (i // (P ** j)) % P for j in range(k) ]
    v = [ sum([ A[y][x] * l[y] for y in range(len(A)) ]) % P for x in range(len(A[0])) ]
    min_w = min(w(v), min_w)
  print("q7:", min_w)

def solve_q6_fill_in_the_blanks(H, P, info, msg):
  H = H.strip()
  A = []
  for line in H.split('\n'):
    v = []
    for col in line:
      v.append(int(col))
    A.append(v)
  k = len(A)
  
  w = lambda v : len([ x for x in v if x != 0 ]) 
  
  assert len(info) == len(msg)
  for i in range(1,P ** k):
    l = [ (i // (P ** j)) % P for j in range(k) ]
    v = [ sum([ A[y][x] * l[y] for y in range(len(A)) ]) % P for x in range(len(A[0])) ]
    
    same = True  
    for j in range(len(info)):
      if v[info[j] - 1] != msg[j]:
        same = False
    if same:
      print("q6 fill in the blanks:", v)
      print("q6 fill in the blanks:", l)
      
def solve_q8(A, B, info, msg, P):
  A = list(map(int,A))
  B = list(map(int,B))
  x = Ints('x1 x2 x3 x4')
  s = Solver()
  s.add(x[0] >= 0)
  s.add(x[1] >= 0)
  s.add(x[2] >= 0)
  s.add(x[3] >= 0)
  s.add(x[info[0] - 1] == msg[0])
  s.add(x[info[1] - 1] == msg[1])
  s.add((x[0] * A[0] + x[1] * A[1] + x[2] * A[2] + x[3] * A[3]) % P == 0)
  s.add((x[0] * B[0] + x[1] * B[1] + x[2] * B[2] + x[3] * B[3]) % P == 0)
  s.check()
  sol = s.model()
  sol = sorted ([(d, sol[d]) for d in sol], key = lambda x: str(x[0]))
  sol = ''.join([ str(d[1].as_long() % P) for d in sol ])
  print("q8:", sol)
 
def solve_q10(P_x_sent, P_x_received_y_sent, P_y_received_x_sent):
  P_y_sent = 1 - P_x_sent
  P_x_received_x_sent = 1 - P_y_received_x_sent
  P_x_received = P_x_received_x_sent * P_x_sent + P_x_received_y_sent * P_y_sent
  print(f"P[x received] = {P_x_received}")
 
 
solve_q1('0-7394-5210-X', 0)
print()
solve_q2_encode('Flow')
solve_q2_correct('11101100 11111010 11100100 11110011')
print()
solve_q3_rref(
"""
100202
012122
002000
""",
3
)
print()
solve_q4_encode(
"""
1111101
0000110
0000001
""", 2, [ 1,5,7 ], [ 1,1,1,0 ])
print()
solve_q5_mul(
"""
110001
101100
011010
""",
"110110",
2
)
print()
 
solve_q6_mul(
2,
"""
11000
00101
10011
""",
[
  ("11101", "00101")
]
)
print()

solve_q6_fill_in_the_blanks(
"""
0110110
0111101
1000101
""",
2,
(1,4,6),
(1,0,1)
)

print()

solve_q7_weight(
"""
010110
110000
011001
""",
2
)
 
print()
solve_q8("0243", "1340", (2,3), (0,3), 5)
print()
solve_q10(0.2, 0.6, 0.8)
 