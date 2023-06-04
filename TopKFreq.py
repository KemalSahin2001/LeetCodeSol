def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    # Create a dictionary of the frequency of each element
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Sort the dictionary by the frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the k most frequent elements
    return [x[0] for x in sorted_freq[:k]]