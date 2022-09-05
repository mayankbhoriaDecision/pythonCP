def printll(head):
    while(head!=None):
        print(head.data)
        head=head.next 

def reversePrint(llist):
    # Write your code here
    if(llist==None):
        print("")
        return None
    else:
        prev=None 
        curr=llist
        while(curr!=None):
            Agla=curr.next 
            curr.next=prev 
            prev=curr
            curr=Agla
        llist=prev
    printll(llist)
