""" In an alien language, surprisingly,
they also use English lowercase letters,
but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language,
and the order of the alphabet,
return true if and only if the given words are sorted lexicographically
in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true

Explanation: As 'h' comes before 'l' in this language,
then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false

Explanation: As 'd' comes after 'l' in this language,
then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false

Explanation: The first three characters "app" match,
and the second string is shorter (in size).
According to lexicographical rules "apple" > "app",
because 'l' > '∅', where '∅' is defined as the blank character
which is less than any other character (More info).

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters. """


class Solution:
    def isAlienSorted(self, words, order: str) -> bool:

        alien_dict = dict()

        for i, chr in enumerate(order):
            alien_dict[chr] = i

        for i in range(len(words) - 1):
            equal = True
            word1 = words[i]
            word2 = words[i + 1]

            for chr1, chr2 in zip(word1, word2):
                if alien_dict[chr1] < alien_dict[chr2]:
                    equal = False
                    break
                elif alien_dict[chr1] > alien_dict[chr2]:
                    return False

            if len(word1) > len(word2) and equal is True:
                return False
        else:
            return True
