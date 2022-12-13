with open("input.txt","r") as f:
    n=14
    stream = [i for i in f.readline()]
    window = stream[:n]
    index=n
    remove_pointer=0
    while True:
        if len(set(window))==n:
            print(index)
            break
        #1 2 3 4, rm 0
        #add 5
        #5 2 3 4, rm 1
        #add 6
        #5 6 3 4, rm 2
        #add 7
        #5 6 7 4, rm 3
        #add 8
        #5 6 7 8, rm 0
        window[remove_pointer]=stream[index]
        index+=1
        remove_pointer=(remove_pointer+1)%n
