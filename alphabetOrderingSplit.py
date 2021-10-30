
def AlphabetOrdering(a):

    b=list(a)
    
    
    numVal=[]
    
    for i in range(len(b)):
    
        numVal.append(ord(b[i]))
  
    diff=[]
    
    for i in range(1,len(b)):
    
        diff.append(  numVal[i] -numVal[i-1]     )
    

    
    splitIndex=[]
    
    for i in range(1,len(b) -1  ):
    
        if(diff[i] * diff[i-1]  <0 ):
    
            splitIndex.append(i+1)
    
    return (len(splitIndex)+1)


