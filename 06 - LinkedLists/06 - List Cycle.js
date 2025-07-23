/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {

  const index = new Map()

  while(head){

    if(index.get(head)) return true
    else index.set(head,1)
    head = head.next

  }  

  return false
};
