class ListNode {
    val
    next 
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}
 

var addTwoNumbers = function(l1, l2) {
    
    const head = new ListNode()
    let result = head
    let resto = false

    while(l1 || l2){

        if(!l1) l1 = new ListNode()
        if(!l2) l2 = new ListNode()

        result.val = l1.val+l2.val;
        if(resto) {
            result.val++
            resto = false
        }
        if (result.val > 9){
            result.val -= 10
            resto = true
        }

        console.log(l1.val, l2.val, result.val)

        l1 = l1.next
        l2 = l2.next

        if ( l1 || l2 ) {

            result.next = new ListNode()
            result = result.next
            
        }
        
    }

    if ( resto ) result.next = new ListNode(1)

    return head

};


const a = new ListNode(9)
const b = new ListNode(9)
const c = new ListNode(9)
const d = new ListNode(9)
const e = new ListNode(9)
const f = new ListNode(9)
const g = new ListNode(9)


const h = new ListNode(9)
const i = new ListNode(9)
const j = new ListNode(9)
const k = new ListNode(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
h.next = i
i.next = j
j.next = k

const util = require('util')
console.log(util.inspect(addTwoNumbers(a,d), false, null, true))
