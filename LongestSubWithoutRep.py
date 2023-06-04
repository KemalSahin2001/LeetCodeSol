def lengthOfLongestSubstring(self,s):
    """
    :type s: str
    :rtype: int
    """


    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    else:
        max = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[j] in s[i:j]:
                    if j-i > max:
                        max = j-i
                    break
                else:
                    if j-i+1 > max:
                        max = j-i+1
        return max