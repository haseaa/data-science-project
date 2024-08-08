class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = ''
        index = 0
        word1_length = len(word1)
        word2_length = len(word2)
        combine_length = word1_length+word2_length
        while True:
            if len(merge) == combine_length:
                break              
            if index < word1_length:
                merge += word1[index]
            if index < word2_length:
                merge += word2[index]
            index += 1

        return merge