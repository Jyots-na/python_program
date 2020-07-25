str ="JYOTSNA"
J =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]
Y =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]
O =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]
T =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]
S =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]
N =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]
A =[[" "for i in range(5)]for j in range(5)]
space=[[" " for i in range(5)] for j in range(5)]

for r in range(5):
    for c in range(5):
        if(c==2 or (r==0 and c!=2)or(r==4 and c<2)):
            J[r][c]="*"
for r in range(5):
    for c in range(5):
        space[r][c]=" "

for r in range(5):
    for c in range(5):
        if(c==2 and r>1) or (r==c and c<2) or (r==0 and c==4) or (r==1 and c==3):
            Y[r][c]="*"
for r in range(5):
    for c in range(5):
        space[r][c]=" "

for r in range(5):
    for c in range(5):
        if(((c==0 or c==4) and (r>=1 and r<=3)) or((r==0 or r==4) and (c>=1 and c<=3))):
            O[r][c]="*"
for r in range(5):
    for c in range(5):
        space[r][c]=" "

for r in range(5):
    for c in range(5):
        if((c==2 and (r>=1 and r<=4)) or (r==0 and (c>=0 and c<=4))):
            T[r][c]="*"
for r in range(5):
    for c in range(5):
        space[r][c]=" "

for r in range(5):
    for c in range(5):
        if(((r==0 or r==2 or r==4) and (c>=1 and c<=3))or (c==0 and r==1)or (c==4 and r==3)):
            S[r][c]="*"
for r in range(5):
    for c in range(5):
        space[r][c]=" "

for r in range(5):
    for c in range(5):
        if(((c==0 or c==4)and (r>=0 and r<=4))or (r==c and (c!=0 and c!=4))):
               N[r][c]="*"
for r in range(5):
    for c in range(5):
        space[r][c]=" "

for r in range(5):
    for c in range(5):
        if(((c==0 or c==4)and (r>=1 and r<=4))or((r==0 or r==2)and(c>=1 and c<=3))):
               A[r][c]="*"


for i in range(5):
    for j in range(5):
        print(J[i][j],end="")
    for j in range(5):
        print(space[i][j],end="")
    for j in range(5):
        print(Y[i][j],end="")
    for j in range(5):
        print(space[i][j],end="")
    for j in range(5):
        print(O[i][j],end="")
    for j in range(5):
        print(space[i][j],end="")
    for j in range(5):
        print(T[i][j],end="")
    for j in range(5):
        print(space[i][j],end="")
    for j in range(5):
        print(S[i][j],end="")
    for j in range(5):
        print(space[i][j],end="")
    for j in range(5):
        print(N[i][j],end="")
    for j in range(5):
        print(space[i][j],end="")
    for j in range(5):
        print(A[i][j],end="")
    print()









