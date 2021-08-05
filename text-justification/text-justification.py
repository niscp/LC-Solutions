class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        while i < len(words):
            j = i + 1
            linelength = len(words[i])
            while j < len(words) and maxWidth > (linelength + len(words[j]) + (j - i - 1)):
                linelength += len(words[j])
                j += 1
            
            rem_spaces = maxWidth - linelength
            no_words = j - i
            if no_words == 1 or j >= len(words):
                result.append(leftJustify(words, rem_spaces, i, j))
            else:
                result.append(midJustify(words, rem_spaces, i, j))
            i = j
        return result
    
def leftJustify(words, diff, i, j):
    extraSpaces = diff - (j - i - 1)
    s = words[i]
    for idx in range(i+1, j):
        s = s + " " + words[idx]
    s = s + " "*extraSpaces
    return s

def midJustify(words, diff, i, j):
    spacesNeeded = j - i - 1
    spaces = diff // spacesNeeded
    ext_spaces = diff % spacesNeeded
    
    s = words[i]
    for idx in range(i+1, j):
        space_here = spaces
        if ext_spaces > 0:
            space_here += 1
            ext_spaces -= 1
        s += " "*space_here + words[idx]
    return s
        

                
                
                
            
            
                
                
        