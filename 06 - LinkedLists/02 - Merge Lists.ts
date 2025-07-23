//Definition for singly-linked list.

class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
 }



function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    
    if(!list1 || !list2) return list1? list1 : list2

    
    
    function merger(list1: ListNode | null, list2: ListNode | null): ListNode | null{

        const headReference = list1
        let current2: ListNode | null = list2
        let current1: ListNode | null = list1.next
        let prev1: ListNode | null = list1

        while(current2 && current1){
            if(current2.val<=current1.val){
                prev1.next = current2
                current2 = current2.next
                prev1.next.next = current1
                prev1 = prev1.next

            }else{
                prev1 = current1
                current1 = current1.next
            }

        }

        if(!current1 && current2){
            prev1.next = current2
        }

        return headReference
    }

    if(list1.val>=list2.val) return merger(list2, list1)
    else return merger(list1, list2)
    
};

const a = new ListNode(1)
const b = new ListNode(2) 
const c = new ListNode(4)

const d = new ListNode(1)
const e = new ListNode(3)
const f = new ListNode(4)

a.next = b
b.next = c

d.next = e
e.next = f

console.log(mergeTwoLists(a, d))
