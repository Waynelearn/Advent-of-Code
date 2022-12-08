with open("input.txt","r") as f:
    Total=0
    for i in f:
        line=i.strip().split(" ")
        Opponent=line[0]
        You=line[1]
        outcome_score={"X":0,"Y":3,"Z":6}
        shape_score={
            "A":{"X":3,"Y":1,"Z":2},
            "B":{"X":1,"Y":2,"Z":3},
            "C":{"X":2,"Y":3,"Z":1}
            }
        Total+=outcome_score[You]+shape_score[Opponent][You]
    print(Total)
