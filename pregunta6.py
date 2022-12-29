def robot(n):    
    if n==1 or n==2:        
        return n    
    return robot(n-1)+robot(n-2)
print(robot(8))