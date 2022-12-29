def sumarecursiva(a,b):    
    if b==0:        
        return a    
    else:        
        return sumarecursiva(a,b-1)+1
print(sumarecursiva(2,5-1)+1)