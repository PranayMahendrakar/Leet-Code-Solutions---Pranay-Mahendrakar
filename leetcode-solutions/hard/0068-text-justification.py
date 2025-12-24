# Problem: Text Justification
# Difficulty: Hard
# URL: https://leetcode.com/problems/text-justification/
# Runtime: 0 ms
# Memory: 12.7 MB

class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                # Justify current line
                spaces = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces)
                else:
                    gaps = len(line) - 1
                    space_per_gap = spaces // gaps
                    extra = spaces % gaps
                    justified = ''
                    for i, w in enumerate(line[:-1]):
                        justified += w + ' ' * (space_per_gap + (1 if i < extra else 0))
                    justified += line[-1]
                    result.append(justified)
                line = []
                line_length = 0
            
            line.append(word)
            line_length += len(word)
        
        # Last line - left justified
        last_line = ' '.join(line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return result