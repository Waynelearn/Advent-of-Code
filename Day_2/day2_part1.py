with open("input2.txt","r") as f:
    Total=0
    for i in f:
        line=i.strip().split(" ")
        Opponent=line[0]
        You=line[1]
        Shape_score={"X":1,"Y":2,"Z":3}
        Outcome={
        "X":{"A":3,"B":0,"C":6},
        "Y":{"A":6,"B":3,"C":0},
        "Z":{"A":0,"B":6,"C":3}
        }
        #draw
        Score=Outcome[You][Opponent]
        Total+=Score+Shape_score[You]
    print(Total)
