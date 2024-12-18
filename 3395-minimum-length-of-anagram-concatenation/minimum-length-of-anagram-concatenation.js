/**
 * @param {string} s
 * @return {number}
 */

var minAnagramLength = function(s) {
    // Function to check if a given length k is valid
    function isValid(k) {
      // Initialize a counter for the first substring of length k
      let prev = countCharacters(s.slice(0, k));
      // Iterate through the string with step k
      for (let i = k; i < s.length; i += k) {
        // Create a counter for the current substring of length k
        let cur = countCharacters(s.slice(i, i + k));
        // Check if the current substring is an anagram of the previous one
        if (!areEqual(prev, cur)) {
          return false;
        }
        prev = cur;
      }
      return true;
    }

    // Function to count the frequency of characters in a string
    function countCharacters(str) {
      const counter = {};
      for (let char of str) {
        counter[char] = (counter[char] || 0) + 1;
      }
      return counter;
    }

    // Function to compare two character frequency objects
    function areEqual(obj1, obj2) {
      const keys1 = Object.keys(obj1);
      const keys2 = Object.keys(obj2);

      if (keys1.length !== keys2.length) return false;

      for (let key of keys1) {
        if (obj1[key] !== obj2[key]) {
          return false;
        }
      }
      return true;
    }

    // Count the frequency of each character in the string
    const charFreq = countCharacters(s);
    // Get the minimum frequency of any character
    const minFreq = Math.min(...Object.values(charFreq));
    // Determine the minimum possible length of the anagram
    const minLength = Math.floor(s.length / minFreq);

    // Check all possible lengths from minLength to s.length
    for (let length = minLength; length <= s.length; length++) {
      // Check if the length is a divisor of s.length and is valid
      if (s.length % length === 0 && isValid(length)) {
        return length;
      }
    }

    return s.length;
  }