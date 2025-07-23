// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
 

function reverseList(head: ListNode | null): ListNode | null {

    if(!head) return null
    let newHead: ListNode | null = null
    
    function recursive(head: ListNode): ListNode {
        if(!head.next){
            newHead = head
            return newHead
        }

        let newNode = recursive(head.next) 
        head.next = null
        newNode.next = head
        return newNode.next
    }
    
    recursive(head)

    return newHead
};
