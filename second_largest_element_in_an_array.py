#Problem link: https://www.geeksforgeeks.org/problems/second-largest3735/1
# brute Force Solution
'''
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        # Selection sort
        for i in range(n - 1):
            max_idx = i
            for j in range(i + 1, n):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]  # sort in descending order

        # Now the array is sorted in descending order
        first = arr[0]
        for i in range(1, n):
            if arr[i] != first:
                return arr[i]  # Second largest found
        return -1  # If no second largest exists

# Better Solution
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        largest = arr[0]

        # First pass: Find the largest
        for i in range(1, n):
            if arr[i] > largest:
                largest = arr[i]

        slargest = -1  # safe because all arr[i] ≥ 1

        # Second pass: Find second largest (distinct from largest)
        for i in range(n):
            if arr[i] != largest and arr[i] > slargest:
                slargest = arr[i]

        # If no second largest found
        return slargest if slargest != -1 else -1
'''
# Optimal Solution
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)

        # Initialize the largest with the first element
        # slargest is set to -1 assuming no second largest exists initially
        largest = arr[0]
        slargest = -1

        # Loop through the array starting from the second element
        for i in range(1, n):
            if arr[i] > largest:
                # Found a new largest, so update second largest to the old largest
                slargest = largest
                largest = arr[i]
            elif arr[i] != largest and arr[i] > slargest:
                # arr[i] is smaller than largest but greater than current second largest
                slargest = arr[i]

        # Return second largest if it was updated, else return -1 (means no second largest)
        return slargest if slargest != -1 else -1
