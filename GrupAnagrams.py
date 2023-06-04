def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    # Create a dictionary to store the anagrams
    anagrams = {}

    # Loop through each word in the list
    for word in strs:

        # Sort the word
        sorted_word = "".join(sorted(word))

        # If the sorted word is not in the dictionary, add it
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]

        # If the sorted word is in the dictionary, append the word to the list
        else:
            anagrams[sorted_word].append(word)

    # Return the values of the dictionary
    return anagrams.values()