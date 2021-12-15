input_coords = [199,200,208,10,200,207,240,269,260,263]

def depth_increase(input_coords):
    total_depth_increase = 0
    for i in range(1,len(input_coords)): #replace with enumerate
        if input_coords[i-1]<input_coords[i]:
            total_depth_increase+=1
    return total_depth_increase
        
print(depth_increase(input_coords))
