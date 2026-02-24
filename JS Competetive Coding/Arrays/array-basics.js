// diff ways to add and remove elements from an array

// push - adds to the end of the array
let arr = [1, 2, 3];
arr.push(4); // arr is now [1, 2, 3, 4]

// pop - removes from the end of the array
arr.pop(); // arr is now [1, 2, 3]

// unshift - adds to the beginning of the array
arr.unshift(0); // arr is now [0, 1, 2, 3]

// shift - removes from the beginning of the array
arr.shift(); // arr is now [1, 2, 3]

// splice - can add or remove elements at any position
arr.splice(1, 0, 1.5); // arr is now [1, 1.5, 2, 3] (adds 1.5 at index 1)
arr.splice(2, 1); // arr is now [1, 1.5, 3] (removes 1 element at index 2)

//Loops
// for loop
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
//while loop
let i = 0;
while (i < arr.length) {
    console.log(arr[i]);
    i++;
}

//inbuilt loops
// for...of loop
for (let num of arr) {
    console.log(num);
}

// forEach loop
arr.forEach(num => console.log(num));

arr.map(num => console.log(num)); // similar to forEach but returns a new array (not used here)

arr.filter(num => num > 1); // returns a new array with elements that satisfy the condition (not used here)

arr.reduce((acc, num) => acc + num, 0); // reduces the array to a single value (not used here)

arr.some(num => num > 2); // returns true if at least one element satisfies the condition (not used here)

arr.every(num => num > 0); // returns true if all elements satisfy the condition (not used here)

arr.find(num => num > 1); // returns the first element that satisfies the condition (not used here)

arr.findIndex(num => num > 1); // returns the index of the first element that satisfies the condition (not used here)

arr.includes(2); // returns true if the array includes the specified element (not used here)

arr.indexOf(2); // returns the index of the first occurrence of the specified element (not used here)

arr.lastIndexOf(2); // returns the index of the last occurrence of the specified element (not used here)

arr.sort((a, b) => a - b); // sorts the array in ascending order (not used here)

arr.reverse(); // reverses the array (not used here)

arr.join(','); // joins the elements of the array into a string with a specified separator (not used here)

arr.slice(1, 3); // returns a shallow copy of a portion of the array (not used here)

arr.splice(1, 2); // removes elements from the array and returns them (not used here)

arr.concat([4, 5]); // returns a new array that is the result of concatenating the original array with another array (not used here)

arr.flat(); // flattens nested arrays into a single array (not used here)

arr.flatMap(num => [num, num * 2]); // maps each element to a new array and flattens the result (not used here)

arr.fill(0); // fills the array with a static value (not used here)

arr.copyWithin(0, 1); // copies a sequence of elements within the array (not used here)

arr.entries(); // returns an iterator of key/value pairs for each index in the array (not used here)

arr.keys(); // returns an iterator of keys (indices) in the array (not used here)

arr.values(); // returns an iterator of values in the array (not used here)

//spread and rest operators
let arr1 = [1, 2, 3];
let arr2 = [...arr1];
console.log(arr2); // arr2 is now [1, 2, 3]

function sum(...nums) { // rest operator to accept variable number of arguments
    return nums.reduce((acc, num) => acc + num, 0);
}
console.log(sum(1, 2, 3)); // returns 6
