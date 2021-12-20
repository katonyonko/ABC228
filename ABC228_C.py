import io
import sys

_INPUT = """\
6
3 1
178 205 132
112 220 96
36 64 20
2 1
300 300 300
200 200 200
4 2
127 235 78
192 134 298
28 56 42
96 120 250
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  P=[]
  for i in range(N):
    tmp=sum(list(map(int,input().split())))
    P.append(tmp)
  X=sorted(P,reverse=True)[K-1]-300
  for i in range(N):
    if P[i]>=X:
      print('Yes')
    else:
      print('No')
  