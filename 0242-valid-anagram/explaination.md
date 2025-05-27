Explaination
So, here we will go for the Counter function which is prints the char as below.

Counter(s) = {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}

Counter creates a dictionary-like object where the keys are elements from the input, and the values are the counts of those elements.

so the compare the two string in the form of dictionary

Time Complexity:
𝑂(m)O(n), where m,𝑛 is the length of the strings.

Space Complexity: 𝑂(𝑘)
O(k), where 𝑘 is the number of unique characters.

Another method(Optimal)
Here, i cretaed a list with length of 26 with all are zeroes and then use for loops for each string and convert them each character cconverted ascii code using ord() and then in other loop with other string, debut the value in list.
So that we can know the characters are present or not. then traverse with forr loop in the list add look for the number other then zero . if it is present then we return False if not we return True

so the Summary:
Time Complexity: O(n+m)

Space Complexity: O(1)
