function elevator(left, right, call){
  if (Math.abs(right-call) >= Math.abs(left-call)) {
      return 'right'
  } else {
      return 'left'
  }
}