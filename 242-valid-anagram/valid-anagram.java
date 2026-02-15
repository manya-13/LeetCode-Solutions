
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] anagram = new int[26];

        if(s.length() != t.length()){
            return false;
        }

        char[] arr1 = s.toCharArray();
        char[] arr2 = t.toCharArray();

        for(char x: arr1){
            anagram[x - 'a'] += 1;
        }

        for(char y: arr2){
            anagram[y - 'a'] -=1; 
            if(anagram[y - 'a'] < 0){
                return false;
            }
        }


        return true;
    }
}