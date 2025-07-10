#problem link: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1

'''
# Brute Force Solution
class Solution:
    def largest(self, arr):
        # Get the size of the array
        n = len(arr)

        # Perform selection sort to sort the array in ascending order
        for i in range(n - 1):
            min_index = i  # Assume the current index holds the minimum

            # Find the index of the smallest element in the unsorted part
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element of the unsorted part
            arr[i], arr[min_index] = arr[min_index], arr[i]

        # After sorting, the largest element will be at the last index
        return arr[-1]
'''

#Optimal Solution
class Solution:
    def largest(self, arr):
        # Get the size of the array
        n = len(arr)

        # Initialize variable to store the largest element
        # Since constraints say arr[i] ≥ 1, starting with 0 is safe
        largest = 0

        # Traverse the array
        for i in range(n):
            # If current element is greater than current largest, update it
            if arr[i] > largest:
                largest = arr[i]

        # Return the largest element found
        return largest
