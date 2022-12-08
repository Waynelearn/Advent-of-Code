
def overlap(A:str,B:str):
    """
    Take in string in the form of min-max for A and B
    Check if B is inside A

    """
    Amin,Amax=A.split("-")
    Amin,Amax=int(Amin),int(Amax)
    Bmin,Bmax=B.split("-")
    Bmin,Bmax=int(Bmin),int(Bmax)
    if Bmin>=Amin and Amax>=Bmax:
        return True
    else:
        False


with open("input.txt","r") as f:
    total=0
    for line in f:
        line=line.strip().split(",")
        if overlap(line[0],line[1]) or overlap(line[1],line[0]):
            total+=1
    print(total)
