/**
 * Definition for Node.
*/
class ListNode {
    val
    next 
    random 
    constructor(val, next, random) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}
 

function copyRandomList(head )  {
    
    const ListNodeindex =  new Map()
    const index = new Map()
    const newList = new ListNode()
    const headReference = head
    let current  = newList
    let counter = 0

    while(head){
        current.val = head.val
        ListNodeindex.set(head, counter)
        head = head.next
        counter++
        if(head){
            current.next = new ListNode()
            current = current.next
        }
    }

    current = newList
    counter = 0

    while(current){
        index.set(counter, current)
        current = current.next
        counter++
    }

    current = newList
    head = headReference


    while(current){
        if(head.random){
            current.random = index.get(ListNodeindex.get(head.random))
        }else{
            current.random = null
        }
        current = current.next
        head = head.next
    }

    return newList
};


const a = new ListNode(7, null)
const b = new ListNode(13)
const c = new ListNode(11)
const d = new ListNode(10)
const e = new ListNode(1)

a.next = b
b.next = c
c.next = d
d.next = e

b.random = a
c.random = e
d.random = c
e.random = a

console.log(copyRandomList(a))
