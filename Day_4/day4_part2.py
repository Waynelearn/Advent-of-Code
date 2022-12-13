
def overlap(A:str,B:str):
    """
    Take in string in the form of min-max for A and B
    Check if A and B overlap

    """
    Amin,Amax=A.split("-")
    Amin,Amax=int(Amin),int(Amax)
    Bmin,Bmax=B.split("-")
    Bmin,Bmax=int(Bmin),int(Bmax)
    #assume A is higher
    if Bmax<Amin or Amax<Bmin:
        return False
    else:
        return True


with open("input1.txt","r") as f:
    total=0
    for line in f:
        line=line.strip().split(",")
        if overlap(line[0],line[1]):
            total+=1
            print(line)
    print(total)
