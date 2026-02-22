var isAnagram = function(s, t) {
    /** Solution 1 */
    // if(s.length !== t.length) {
    //     return false;
    // }
    // let s_sorted = s.split("").sort().join("");
    // let t_sorted = t.split("").sort().join("");
    // return s_sorted === t_sorted;

    /** Solution 2 */
    if(s.length !== t.length) {
        return false;
    }
    let s_obj = {};
    let t_obj = {};
    for (let i=0; i < s.length; i++) {
        s_obj[s[i]] = (s_obj[s[i]] || 0) + 1;
        t_obj[t[i]] = (t_obj[t[i]] || 0) + 1;
    }
    for (let key in s_obj) {
        if (s_obj[key] !== t_obj[key]) {
            return false;
        }
    }
    return true;
};

console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram("rat", "car"));