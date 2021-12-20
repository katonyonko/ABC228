import io
import sys

_INPUT = """\
6
4 2
3 1 1 2
20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  X-=1
  A=list(map(int,input().split()))
  know=[False]*N
  ans=0
  while know[X]==False:
    know[X]=True
    ans+=1
    X=A[X]-1
  print(ans)