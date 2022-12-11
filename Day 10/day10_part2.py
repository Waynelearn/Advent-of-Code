def pixel(x,col):
    if x-1<=col and col<=x+1:
        return "#"
    else:
        return "."
res=[]
x=1
row=0
col=0
img=[""]
with open("input.txt","r") as f:
    
    for line in f:
        line = line.strip("\n").split(" ")
        first=line[0]
        if col%40==0:
            col=0
            row+=1
            img.append("")
        
        
        if first=="addx":
            for i in range(2):
                img[row]+=pixel(x,col)
                
                #move sprite
                if i==1:
                    x+=int(line[1])
                col+=1
                
            
        elif first=="noop":
            
            
            img[row]+=pixel(x,col)
            col+=1
        
for row in img:
    print(row)



