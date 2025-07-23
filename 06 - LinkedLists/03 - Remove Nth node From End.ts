/**
 * Definition for singly-linked list.
 */
 class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
 }
 

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {

    let endingNode: ListNode|null = head
    let deletedNode: ListNode|null = head
    let previousNode: ListNode|null = head
    
    //offset
    let counter:number = 0

    while(counter != n-1){
        endingNode = endingNode.next
        counter++
    }

    if(!endingNode.next){
        return head.next
    }

    while(endingNode.next){
        
        endingNode = endingNode.next
        deletedNode = deletedNode.next
        
        if(counter>=n){
            previousNode = previousNode.next
        }

        counter++
    }

    previousNode.next = deletedNode.next
    

    return head
};
