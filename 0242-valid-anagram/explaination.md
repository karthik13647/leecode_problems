# Anagram Checker

## Explanation

### Method 1: Using `Counter` Function
The `Counter` function from the `collections` module creates a dictionary-like object where the keys are elements from the input, and the values are the counts of those elements.

#### Example:
```python
Counter(s) = {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
```

The comparison checks if two strings have identical character frequencies by comparing the resulting dictionaries.

#### Time Complexity:
- **\(O(m + n)\):** where \(m\) and \(n\) are the lengths of the two strings.

#### Space Complexity:
- **\(O(k)\):** where \(k\) is the number of unique characters in the strings.

### Method 2: Using a Fixed-Size Array (Optimal)
In this method:
1. Create a list of size 26 (corresponding to the English alphabet) initialized with zeros.
2. Traverse the first string and increment the corresponding index for each character using `ord()`.
3. Traverse the second string and decrement the corresponding index for each character.
4. Check the list for any non-zero values to determine if the strings are anagrams.

#### Summary:
- **Time Complexity:** \(O(n + m)\)
- **Space Complexity:** \(O(1)\)

### Key Insights:
- The `Counter` method is more Pythonic but requires additional space for the dictionary.
- The fixed-size array method is optimal in terms of space, utilizing constant space regardless of the input size.
