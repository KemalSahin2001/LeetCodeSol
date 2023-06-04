def isAnagram(self, s, t):
    # Check if the lengths of the strings are equal
    if len(s) != len(t):
        return False

    # Create dictionaries to count the frequency of characters in both strings
    count_s = {}
    count_t = {}

    # Count the frequency of characters in string s
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    # Count the frequency of characters in string t
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Check if the character frequencies are the same in both strings
    return count_s == count_t