var deleteDuplicates = function (head) {
  let headcpy = head;
  if (head == null) {
    return head;
  }
  if (head.next == null) {
    return head;
  }
  let left = head;
  let right = head.next;
  while (right != null) {
    if (left.val == right.val) {
      left.next = right.next;
      right = left.next;
    } else {
      left = left.next;
      right = right.next;
    }
  }
  return headcpy;
};
