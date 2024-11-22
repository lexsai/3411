from math import *

def fact(n):
  return prod(range(1,n+1))

def C(n, k):
  return fact(n) / (fact(n - k) * fact(k))

def ISBN(A):
  return sum([ a*b for (a,b) in zip(A, range(1,len(A)+1)) ]) % 11

def mdiv(a, b, m):
  if b == 0:
    return 0

  if a < 0:
    a = -a
    b = -b

  b %= m
  while a > m:
    a -= m

  return (m * mdiv(m, -b, a) + b) // a

class GFMatrix:
  def __init__(self, P, m):
    self.P = P
    self.m = m
  
  def width(self):
    return len(self.m[0])
  
  def height(self):
    return len(self.m)
  
  def copy(self):
    r = []
    
    for row in self.m:
      v = []
      for col in row:
        v.append(col)
      r.append(v)
    
    return GFMatrix(self.P, r)
  
  def row_add(self, a, b, k):
    B = self.copy()
    for i in range(B.width()):
      B.m[a][i] = (B.m[a][i] + B.m[b][i] * k) % self.P
    return B

  def row_set(self, a, k):
    B = self.copy()
    for i in range(B.width()):
      B.m[a][i] = (B.m[a][i] * k) % self.P
    return B
  
  def transpose(self):
    B = []
    
    for i in range(self.width()):
      v = []
      for j in range(self.height()):
        v.append(self.m[j][i])
      B.append(v)
    
    return GFMatrix(self.P, B)
  
  def row_echelon_form(self):
    H = self.copy()
    for i in range(self.height()):
      for lead in range(self.width()):
        if H.m[i][lead] == 0:
          continue
        
        if H.m[i][lead] != 1:
          H = H.row_set(i, mdiv(H.m[i][lead], H.m[i][lead], self.P))
        
        for j in range(self.height() - 1, i, -1):
          if H.m[j][lead] == 0:
            continue
          H = H.row_add(j, i, -mdiv(H.m[j][lead], H.m[i][lead], self.P))
        break
    return H

  def reduced(self):
    H = self.copy()
    for i in range(1, self.height()):
      for lead in range(self.width()):
        if H.m[i][lead] == 0:
          continue
        for j in range(i - 1, -1, -1):
          if H.m[j][lead] == 0:
            continue
          H = H.row_add(j, i, -mdiv(H.m[j][lead], H.m[i][lead], self.P))
        break
    return H
  
  def mul(self, B):
    C = []
    
    for i in range(self.height()):
      v = []
      for j in range(B.width()):
        S = 0
        for k in range(self.width()):
          S = (S + self.m[i][k] * B.m[k][j]) % self.P
        v.append(S)
      C.append(v)
    
    return GFMatrix(self.P, C)
  
  def show(self):
    for row in self.m:
      print(''.join(map(str, row)))
