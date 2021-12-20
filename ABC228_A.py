import io
import sys

_INPUT = """\
6
7 20 12
20 7 12
23 0 23
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S,T,X=map(int,input().split())
  if S<T:
    if S<=X<T:
      print('Yes')
    else:
      print('No')
  else:
    if S<=X or X<T:
      print('Yes')
    else:
      print('No')