class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Start from the rightmost bits
        i, j = len(a) - 1, len(b) - 1

        # Iterate through both binary strings
        while i >= 0 or j >= 0 or carry:
            # Get the current bits or 0 if out of bounds
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum and carry
            current_sum = bit_a + bit_b + carry
            carry = current_sum // 2

            # Append the current bit to the result
            result.append(str(current_sum % 2))

            # Move to the next bits towards the left
            i -= 1
            j -= 1

        # Reverse the result since we built it from right to left
        result.reverse()

        return ''.join(result)
        