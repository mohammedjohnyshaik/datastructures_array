class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Check edge cases where numRows is 1 or greater than or equal to the length of the string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize an array to represent each row
        result = [''] * numRows
        index = 0
        direction = 1  # Direction variable to determine whether to move up or down in rows

        # Iterate through each character in the string
        for char in s:
            # Place the character in the current row
            result[index] += char

            # Change the direction when reaching the first or last row
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1

            # Move to the next row based on the direction
            index += direction

        # Concatenate the rows to get the final zigzag pattern
        final_result = ''.join(result)
        return final_result

# Example usage:
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))  # Output: "A"
