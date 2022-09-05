def insertNodeAtTail(head, data):
    
    
    if(head==None):
        head=SinglyLinkedListNode(data)    
        head.next=None
        
        return head
        
    else:
        
        tmp=head
        
        while(tmp.next!=None):
            tmp=tmp.next 
        
        newnode=SinglyLinkedListNode(data)    
        
        tmp.next=newnode
     
        
        return head
