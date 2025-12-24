# Problem: Substring with Concatenation of All Words
# Difficulty: Hard
# URL: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Runtime: 31 ms
# Memory: 13.2 MB

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            curr_count = {}
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1
                    
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        result.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = right
        
        return result