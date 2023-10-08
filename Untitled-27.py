n=int( input("svp entrer un nombre positif non nul") )
if n<0 or n==0:
    print("le nombre doit etre positif et non nul")
else:
 for i in range (1,n):
    if n%i==0:
        print(i)