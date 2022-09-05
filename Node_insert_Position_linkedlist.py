def insertNodeAtPosition(llist, data, position):
    # Write your code here
    
    if(llist!=None):
        tmp=llist
        
        count=1
        
        
        while(tmp!=None):
            
            if(count==position):
                
                new=SinglyLinkedListNode(data)
                
                val=tmp.next
                
                tmp.next=new 
                
                new.next=val
                
                return llist
                
            else:
                count+=1
                tmp=tmp.next
        
    else:
        
        new=SinglyLinkedListNode(data)
        llist=new
        return llst
