n=int(input())
w=list(map(int, input().split()))
x=int(input())
w.sort()
s,e,c=0,n-1,0
while s!=e:
  sum=w[s]+w[e]
  if sum>x:
    e-=1
  elif sum<x:
    s+=1
  elif sum==x:
    c+=1
    s+=1
print(c)