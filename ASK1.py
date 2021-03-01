import random

tetdiagwnia=0
tetor=0
tetka8=0

w=input("dwste diastaSEIS")
h=w
f=0
w=int(w)
h=int(h)
b=0
plh8os_tesewn=w*h
print("to plh8os 8esewn einai")
print(plh8os_tesewn)
for c in range(100):
 Matrix = [[0 for y in range(h)] for x in range(w)]

 misospinakas=plh8os_tesewn//2
 for f in range(misospinakas ):
  x=int(random.uniform(0,h))
  y=int(random.uniform(0,w))
  while ( Matrix[x][y]==1):
      x=int(random.uniform(0,h))
      y=int(random.uniform(0,w))
  Matrix[x][y]=1
 for i in range(len(Matrix)):
  pl=int(0)
  for j in range(len(Matrix)):
   if Matrix[i][j]==1:
    pl=pl+1
    if pl>3:
        tetor=tetor+1
   else:
        pl=0
 for j in range(len(Matrix)):
  pl=int(0)
  for i in range(len(Matrix)):
   if Matrix[i][j]==1:
       pl=pl+1
       if pl>3:
           tetka8=tetka8+1
   else:
      pl=0
 max_col=len(Matrix[0])
 max_row=len(Matrix)
 fdiag=[[] for _  in range(max_row + max_col-1) ]
 bdiag=[[] for _ in range(len(fdiag)) ]
 min_bdiag= -max_row + 1
 for x in range(max_col):
  for y in range (max_row):
   fdiag[x+y].append(Matrix[y][x])
   bdiag[x-y-min_bdiag].append(Matrix[y][x])
 bhma=int(0)
 for p in range (h):
     pl1=0
     if bhma < h:
      bhma=bhma+1
     else:
         bhma=bhma+1
     for m in range((bhma)):
         if int(fdiag[p][m])==1:
             pl1=pl1+1
             if pl1>3:
                 tetdiagwnia=tetdiagwnia+1
         else:
             pl1=0
 bhma=w
 for p in range (h,(w*h-1)):
     pl1=0
     bhma=bhma-1
     for m in range(0,bhma):
         if int(fdiag[p][m])==1:
             pl1=pl1+1
             if pl1>3:
                 tetdiagwnia=tetdiagwnia+1
         else:
             pl1=0
 bhma2=int(0)
 for g in range(h):
     pl1=0
     if bhma2<h:
         bhma2=bhma2+1
     else:
         bhma2=bhma2-1
     for n in range(bhma2):
         if bdiag[g][n]==1:
             pl1=pl1+1
             if pl1 > 3:
                 tetdiagwnia=tetdiagwnia+1
         else:
                 pl1=0
 bhma2=w
 for g in range(h,(w*h-1)):
     pl1=0
     bhma2=bhma2-1
     for n in range(0,bhma2):
         if bdiag[g][n]==1:
             pl1=pl1+1
             if pl1 > 3:
                 tetdiagwnia=tetdiagwnia+1
         else:
                 pl1=0


print("ο μεσος ορος τετραδων απο ασους στις διαγωνιους ειναι ")
print(tetdiagwnia/100)
print("ο μεσος ορος τετραδων απο ασους οριζοντια ειναι ")
print(tetor/100)
print("ο μεσος ορος τετραδων απο ασους καθετα ειναι ")
print(tetka8/100)
