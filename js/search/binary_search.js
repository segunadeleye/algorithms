/**
 * Returns true if the value is in the array
 * Otherwise, returns false
 *
 * @param {number[]} array
 * @param {number} value
 *
 * @returns {boolean}
 */
let binarySearchRecursion = (array, value) => {
  if (!array.length) return false;

  let midpoint = parseInt(array.length / 2);
  if (array[midpoint] === value) {
      return true
  } else {
    if (array[midpoint] > value) {
      newArray = array.slice(0, midpoint)
    } else {
      newArray = array.slice(midpoint + 1)
    }
    return binarySearchRecursion(newArray, value)
  }
}

/**
 * Returns the first index position of the value in the array.
 * Otherwise returns -1
 *
 * @param {number[]} array - Great
 * @param {number[]} value
 *
 * @returns {number}
 */
var binarySearchWhileLoop = (array, value) => {
  let left = 0,
      right = array.length - 1;

  while (left <= right) {
    let midpoint = Math.floor((left + right) / 2);
    if (array[midpoint] > value) {
      right = midpoint - 1;
    } else if (array[midpoint] < value) {
      left = midpoint + 1;
    } else {
      return midpoint;
    }
  }
  return -1;
}

function binarySearch4(array, value) {
  let newArray = array;
  let haystack = Math.floor(array.length / 2)

  console.log(haystack, array[haystack])
  if (array[haystack] > value) {
    newArray = array.slice(0, haystack)
    return binarySearch4(newArray, value)
  } else if (array[haystack] < value) {
    newArray = array.slice(haystack + 1, array.length)
    console.log(newArray)
    return binarySearch4(newArray, value)
  } else {
    return haystack
  }
}
