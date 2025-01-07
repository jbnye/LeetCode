class Solution(object):
    def reverseVowels(self, s):
        vowels = []
        count = 0
        l = list(s)
        for x in range(len(s)):
            if (l[x] in 'AaEeIiOoUu'):
                vowels.append(l[x])
        vowels = vowels[::-1]
        for x in range(len(s)):
            if (l[x] in 'AaEeIiOoUu'):
                l[x] = vowels[count]
                count += 1
        return ''.join(l)