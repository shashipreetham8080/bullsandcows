secret=input("enter secret number")
guess=input("enter guess number")

secretList=[d for d in str(secret)]
guessList=[d for d in str(guess)]
print(secretList)
print(guessList)
x=0
y=0
sset=set()
gset=set()
for i,d in enumerate(secretList):
    sset.add((i,d))
for i,d in enumerate(guessList):
    gset.add((i,d))
res = sset.intersection(gset)
x=len(res)
for item in res:
    secretList[item[0]]=-1 
    guessList[item[0]]=-1
bctr,cctr=0,0

for i,d in enumerate (secretList):
    if d in guessList:
        if secretList[i]==guessList[i]:
            bctr+=1
        else:
            cctr+=1
            ind=guessList.index(d)
            guessList[ind]=-2
            secretList[i]=-2
ans=(str(bctr)+"bulls"+str(cctr)+"cows")
print(ans)

