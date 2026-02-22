const isPalindrome = (x) => {
    if ( x < 0 || (x % 10 === 0 && x !== 0) ) {
        return false;
    }
    return x === +x.toString().split('').reverse().join('');
}

console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));