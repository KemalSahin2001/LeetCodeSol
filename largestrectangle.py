def largestRectangleArea(heights):
    if len(heights) == 0:
        return 0

    minimum = min(heights)
    index = heights.index(minimum)

    area = minimum * len(heights)

    left = heights[:index]
    right = heights[index+1:]

    area = max(area,largestRectangleArea(left), largestRectangleArea(right))

    return area


heights = [2, 4]
print(largestRectangleArea(heights))
