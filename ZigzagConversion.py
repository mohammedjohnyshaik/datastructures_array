class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # Initializing an array of empty strings to represent each row
        rows = [''] * numRows
        index, step = 0, 1
        # Iterating through each character in the string
        for char in s:
            rows[index] += char
            # Changing the direction when reaching the first or last row
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            # Moving to the next row
            index += step

        # Concatenating the rows to get the final zigzag pattern
        result = ''.join(rows)
        return result

# Example usage:
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  
print(solution.convert("PAYPALISHIRING", 4))  
print(solution.convert("A", 1))  
