class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        braces_map = {"]":"[", "}":"{", ")":"("}
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                st.append(s[i])
            else:
                if len(st) >0:
                    if braces_map.get(s[i]) == st.pop():
                        continue
                    else:
                        return False
                else:
                    return False
        if len(st) == 0:
            return True
        return False
        