def deleteNode(llist, position):
    # Write your code here
    
    
    count=0
    
    if(llist!=None):
        
        tmp=llist
        
        while(tmp!=None):
            
            
            
            if(position>0):
                
                if( count==position-1):
                
                    delv=tmp.next 
                
                
                    tmp.next=delv.next 
                
                    return llist
                
                else:
                    tmp=tmp.next
                    count+=1     
                    
            else:
                if(position==0):
                        
                    llist=llist.next
                        
                    return llist
                                
    else:
        return None
                
