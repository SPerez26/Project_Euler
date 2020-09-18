#Problem28

spiral_side = 1001
size = spiral_side**2
diagonal = []
counter = 0

start = 3
step = 2
end = (start + step*3) + 1

while counter < size:
    for i in range(start,end,step):
        #counter += 1
        #print(i,start,step,end,counter)
        #if counter == 25:
            #break
        diagonal.append(i)
            
    counter = i
        
    step +=2
    start = i + step
    end = (start + step*3) + 1
    #print("END","Counter:",counter)
    
diagonal1 = []
diagonal2 = []
    
for i in range(1,len(diagonal)+1,2):
    diagonal1.append(diagonal[i])
    
for i in range(0,len(diagonal),2):
    diagonal2.append(diagonal[i])
    
diagonal1.append(1)
diagonal2.append(1)

diagonal1.sort(reverse=False)
diagonal2.sort(reverse=False)
#print(diagonal1)
#print(diagonal2)
print(f"Sum of numbers in diagonals: {sum(diagonal1)+sum(diagonal2)-1}")