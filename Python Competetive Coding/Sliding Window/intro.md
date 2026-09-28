Sliding Window Technique
Sliding Window Technique is a method used to solve problems that involve subarray or substring or window.

- Instead of repeatedly iterating over the same elements, the sliding window maintains a range (or “window”) that moves step-by-step through the data, updating results incrementally.
- The main idea is to use the results of previous window to do computations for the next window.
- Commonly used for problems like finding subarrays with a specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently.


Example Problem - Maximum Sum of a Subarray with K Elements
Given an array arr[] and an integer k, we need to calculate the maximum sum of a subarray having size exactly k.

Input  : arr[] = [5, 2, -1, 0, 3], k = 3
Output : 6
Explanation : We get maximum sum by considering the subaarray [5, 2 , -1]

Input  : arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 
Output : 39
Explanation : We get maximum sum by adding subarray [4, 2, 10, 23] of size 4.

import sys

def maxSum(arr, n, k):
    # Initialize result
    max_sum = -sys.maxsize

    # Consider all blocks starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]

        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    n = len(arr)
    print(maxSum(arr, n, k))


[Expected approach] Sliding Window Technique - O(n) Time and O(1) Space

def maxSum(arr, k):
    
    # length of the array
    n = len(arr)

    # n must be greater than k
    if n <= k:
        print("Invalid")
        return -1

    # Compute sum of first window of size k
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum

    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(maxSum(arr, k))