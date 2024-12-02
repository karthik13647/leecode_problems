class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int start = 0 ;

        int end = s.length()-1;

        while (start<end){
            while (start < end && !isVowel(chars[start])) {
                start++;
            }

            while (start < end && !isVowel(chars[end])) {
                end--;
            }

            if (start < end) {
                swap(chars, start, end);
                start++;
                end--;
            }

        }

        return new String(chars);
    }

    public void swap(char[] word, int start, int end){
        char temp = word[start];
        word[start] = word[end];
        word[end] = temp;
    }
    public boolean isVowel(char c){
        return c=='a' || c=='e' || c=='o' ||c=='i'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
    }
}