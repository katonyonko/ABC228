import io
import sys

_INPUT = """\
6
2 2 2
3 14 15926535
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,K,M=map(int,input().split())
  if M%mod==0:
    print(0)
  else:
    r=pow(K,N,mod-1)
    print(pow(M,r,mod))