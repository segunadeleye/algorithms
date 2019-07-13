var insertionSort = (arr) => {
  for (var i = 1; i < arr.length; i++) {
    var move = arr[i];
    for (var j = i; j > 0; j--) {
      var compare = arr[j - 1]
      if (move < compare) {
        arr[j] = compare;
        arr[j - 1] = move;
      }
    }
  }
  return arr;
}
