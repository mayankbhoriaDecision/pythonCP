def subLinkedList(l1, l2): 
    # Code here
    # return head of difference list
    
    
    str1=''
    
    str2=''
    
    while(l1 is not None):
        
        str1+=str(l1.data)
        
        l1=l1.next
        
    while(l2 is not None):
        
        str2+=str(l2.data)
        
        l2=l2.next


    val1=int(str1)
    
    val2=int(str2)
    
    num=val1-val2
    
    if(num<0):
        num=num*-1
        
    res=LinkedList()
    
    ul=list(str(num))
    
    for x in ul:
        
        res.insert(int(x))
    
    
    return res.head
