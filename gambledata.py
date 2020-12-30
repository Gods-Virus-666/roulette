z=1
data=[]
while z != 0 :
    x=input("How many plays: ")
    y=int(x)
    data.append(y)
    data.sort()
    print("# of times before win: "+ str(data))
