""" Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters. """


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic_mag = dict()

        for chr in magazine:
            if chr not in dic_mag:
                dic_mag[chr] = 1
            else:
                dic_mag[chr] += 1

        for chr in ransomNote:
            if chr not in dic_mag:
                return False
            else:
                if dic_mag[chr] == 0:
                    return False
                else:
                    dic_mag[chr] -= 1

        return True
