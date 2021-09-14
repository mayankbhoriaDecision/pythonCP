using System;
 
// This class represents a single node 
// in a linked list
class Node 
{
    public int data;
    public Node next;
     
    public Node(int data)
    {
        this.data = data;
        this.next = null;
    }
}
 
// This is a utility class for linked list
class LLUtil
{
    
    // This function creates a linked list
    // from a given array and returns head
    public Node createLL(int[] arr)
    {
        Node head = new Node(arr[0]);
        Node temp = head;
         
        Node newNode = null;
        for(int i = 1; i < arr.Length; i++)
        {
            newNode = new Node(arr[i]);
            temp.next = newNode;
            temp = temp.next;
        }
        return head;
    }
    
    // This function prints given linked list
    public void printLL(Node head)
    {
        while (head != null)
        {
            Console.Write(head.data + " ");
            head = head.next;
        }
        Console.WriteLine();
    }
}

class GFG{

// Driver Code
public static void Main(string[] args)
{
    int[] arr = { 12, 15, 10, 11, 5, 6, 2, 3 };
    
    LLUtil llu = new LLUtil();
    Node head = llu.createLL(arr);
    
    Console.WriteLine("Given Linked List");
    llu.printLL(head);
    deleteNodesOnRightSide(head);
    
    Console.WriteLine("Modified Linked List");
    llu.printLL(head);
}
 
// Main function
public static void deleteNodesOnRightSide(Node head)
{

    Node temp = head;
    
    while (temp != null && temp.next != null)
    {
        
        // Copying next node data into current node
        // i.e. we are indirectly deleting current node
        if (temp.data < temp.next.data)
        {
            temp.data = temp.next.data;
            temp.next = temp.next.next;
        }
        else
        {
            
            // Move to the next node
            temp = temp.next;
        }
    }
}
}

// This code is contributed by rutvik_56
