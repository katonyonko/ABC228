import io
import sys

_INPUT = """\
6
3 4 2 3 3 1
3 1 4 1
5 9 2 6
5 3 5 8
3 4 2 3 3 4
3 1 4 1
5 9 2 6
5 3 5 8
10 10 3 7 2 3
9 7 19 7 10 4 13 9 4 8
10 15 16 3 18 19 17 12 13 2
12 18 4 9 13 13 6 13 5 2
16 12 2 14 18 17 14 7 8 12
12 13 17 12 14 15 19 7 13 15
5 2 16 10 4 6 1 2 7 8
10 14 14 10 9 13 11 4 9 19
16 12 3 19 19 6 2 19 14 20
15 3 19 19 2 10 1 4 3 15
13 20 5 6 19 1 7 17 10 19
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def sliding_window(A,L):
    """
    A: 列のi番目の要素
    L: 最小値を調べる長さ
    """
    ans = []
    que = deque()
    for i, a in enumerate(A):
      while que and a <= que[-1][1]:
        que.pop()
      que.append((i, a))
      ans.append(que[0][1])
      if que and que[0][0] <= i+1-L:
        que.popleft()
    return ans[L-1:]

  H,W,h1,w1,h2,w2=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(H)]
  h2,w2=min(h1,h2),min(w1,w2)
  AA=[0]*(W+1)
  for i in range(H):
    AA.append(0)
    for j in range(W):
      AA.append(A[i][j]+AA[-1]+AA[i*(W+1)+j+1]-AA[i*(W+1)+j])
  T=[AA[(i+h1)*(W+1)+j+w1]-AA[i*(W+1)+j+w1]-AA[(i+h1)*(W+1)+j]+AA[i*(W+1)+j] for i in range(H-h1+1) for j in range(W-w1+1)]
  A=[-AA[(i+h2)*(W+1)+j+w2]+AA[i*(W+1)+j+w2]+AA[(i+h2)*(W+1)+j]-AA[i*(W+1)+j] for i in range(H-h2+1) for j in range(W-w2+1)]
  MM=[]
  for i in range(H-h2+1):
    MM+=sliding_window(A[i*(W-w2+1):(i+1)*(W-w2+1)],w1-w2+1)
  MM=[MM[i*(W-w1+1)+j] for j in range(W-w1+1) for i in range(H-h2+1)]
  MM2=[]
  for i in range(W-w1+1):
    MM2+=sliding_window(MM[i*(H-h2+1):(i+1)*(H-h2+1)],h1-h2+1)
  MM2=[MM2[i*(H-h1+1)+j] for j in range(H-h1+1) for i in range(W-w1+1)]
  print(max([T[i]+MM2[i] for i in range((H-h1+1)*(W-w1+1))]))