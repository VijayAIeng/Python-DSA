"""
COMPLEXITY ANALYSIS - Complete Guide with Examples
Interview Focus: Understanding Big O, Big Omega, Big Theta
"""

import time
import math
from typing import List, Any

# ============================================
# 1. TIME COMPLEXITY CLASSES
# ============================================

class ComplexityAnalysis:
    """
    Complete guide to time and space complexity analysis
    """
    
    @staticmethod
    def constant_time_examples():
        """
        O(1) - Constant Time
        - Accessing array element by index
        - Hash table lookup
        - Mathematical operations
        
        Interview Question: Is accessing an element in a dictionary O(1)?
        Answer: Average case O(1), worst case O(n) due to hash collisions
        """
        def constant_time_ops(arr: List[int], target: int) -> int:
            # O(1) - Array access
            first = arr[0]
            
            # O(1) - Arithmetic
            result = (target * 2) // 3
            
            # O(1) - Dictionary lookup
            cache = {1: "one", 2: "two"}
            value = cache.get(target, "not found")
            
            # O(1) - Conditional check
            if target > 0:
                return target
            return -1
        
        # Space complexity: O(1) - using constant extra space
        return constant_time_ops
    
    @staticmethod
    def logarithmic_time_examples():
        """
        O(log n) - Logarithmic Time
        - Binary Search
        - Balanced BST operations
        - Binary heap operations
        
        Interview Question: Why does binary search have O(log n)?
        Answer: We halve the search space each step
        """
        def binary_search(arr: List[int], target: int) -> int:
            """
            O(log n) time, O(1) space
            Works only on sorted arrays
            """
            left, right = 0, len(arr) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1  # Search right half
                else:
                    right = mid - 1  # Search left half
            
            return -1  # Not found
        
        return binary_search
    
    @staticmethod
    def linear_time_examples():
        """
        O(n) - Linear Time
        - Single loop through n elements
        - Linear search
        - Array traversal
        """
        def linear_search(arr: List[int], target: int) -> int:
            """
            O(n) time, O(1) space
            Works on any array
            """
            for i, value in enumerate(arr):
                if value == target:
                    return i
            return -1
        
        def find_max(arr: List[int]) -> int:
            """
            O(n) time, O(1) space
            """
            if not arr:
                return None
            
            max_val = arr[0]
            for num in arr:
                if num > max_val:
                    max_val = num
            return max_val
        
        return linear_search
    
    @staticmethod
    def linearithmic_time_examples():
        """
        O(n log n) - Linearithmic Time
        - Merge Sort
        - Quick Sort
        - Heap Sort
        
        Interview Question: Why is O(n log n) considered efficient?
        Answer: It's the optimal time for comparison-based sorting
        """
        def merge_sort(arr: List[int]) -> List[int]:
            """
            O(n log n) time, O(n) space
            Stable sorting algorithm
            """
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        return merge_sort
    
    @staticmethod
    def quadratic_time_examples():
        """
        O(n²) - Quadratic Time
        - Nested loops over same collection
        - Bubble Sort, Selection Sort
        - Naive pattern matching
        
        Interview Question: When is O(n²) acceptable?
        Answer: For small n, or when n is bounded
        """
        def bubble_sort(arr: List[int]) -> List[int]:
            """
            O(n²) time, O(1) space
            """
            n = len(arr)
            arr = arr.copy()
            
            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                if not swapped:
                    break
            
            return arr
        
        return bubble_sort

# ============================================
# 2. SPACE COMPLEXITY ANALYSIS
# ============================================

class SpaceComplexity:
    """
    Understanding memory usage in algorithms
    """
    
    @staticmethod
    def space_complexity_examples():
        """
        Important: Space complexity includes both auxiliary space and input space
        """
        
        def in_place_operation(arr: List[int]) -> None:
            """
            O(1) auxiliary space
            Modifies input array directly
            """
            for i in range(len(arr)):
                arr[i] *= 2
        
        def create_new_array(arr: List[int]) -> List[int]:
            """
            O(n) auxiliary space
            Creates new array of same size
            """
            return [x * 2 for x in arr]
        
        def recursive_factorial(n: int) -> int:
            """
            O(n) space due to recursion stack
            Each recursive call adds to call stack
            """
            if n <= 1:
                return 1
            return n * recursive_factorial(n - 1)
        
        def two_dimensional_memory(n: int, m: int) -> List[List[int]]:
            """
            O(n*m) space for 2D array
            """
            return [[0] * m for _ in range(n)]
    
    @staticmethod
    def common_space_complexities():
        """
        Common space complexity classes:
        - O(1): Constant - variables, pointers
        - O(log n): Recursive binary search
        - O(n): Arrays, strings, recursion depth
        - O(n²): 2D arrays, matrices
        """
        pass

# ============================================
# 3. AMORTIZED ANALYSIS
# ============================================

class AmortizedAnalysis:
    """
    Understanding amortized time complexity
    """
    
    @staticmethod
    def dynamic_array_example():
        """
        Python list uses amortized O(1) for append
        - Resizing occasionally causes O(n) operation
        - Over many operations, average is O(1)
        """
        arr = []
        for i in range(1000):
            arr.append(i)  # Amortized O(1)
            
        # Python list resizing strategy: 
        # - Overallocate by ~12.5%
        # - Capacity grows: 0, 4, 8, 16, 25, 35, 46, ...
        
    @staticmethod
    def amortized_operations():
        """
        Other amortized O(1) operations:
        - Stack push/pop
        - Queue enqueue/dequeue (using two stacks)
        - Union-Find with path compression
        """

# ============================================
# 4. COMPLEXITY COMPARISON TABLE
# ============================================

class ComplexityComparison:
    """
    Quick reference for common operations
    """
    
    # ==================== ARRAYS ====================
    array_operations = """
    Operation        | Time        | Space
    ---------------|-------------|-------
    Access by index | O(1)        | O(1)
    Search          | O(n)        | O(1)
    Insert at end   | O(1)*       | O(1)
    Insert at start | O(n)        | O(1)
    Delete at end   | O(1)        | O(1)
    Delete at start | O(n)        | O(1)
    *Amortized constant time
    """
    
    # ==================== LINKED LISTS ====================
    linked_list_operations = """
    Operation        | Singly LL   | Doubly LL
    ---------------|-------------|-----------
    Access by index | O(n)        | O(n)
    Search          | O(n)        | O(n)
    Insert at head  | O(1)        | O(1)
    Insert at tail  | O(n)        | O(1)*
    Delete at head  | O(1)        | O(1)
    Delete at tail  | O(n)        | O(1)*
    *With tail pointer
    """
    
    # ==================== HASH TABLES ====================
    hash_table_operations = """
    Operation        | Average   | Worst
    ---------------|-----------|--------
    Insert          | O(1)      | O(n)
    Delete          | O(1)      | O(n)
    Search          | O(1)      | O(n)
    """
    
    # ==================== BINARY SEARCH TREES ====================
    bst_operations = """
    Operation        | Average   | Worst (unbalanced)
    ---------------|-----------|-------------------
    Search          | O(log n)  | O(n)
    Insert          | O(log n)  | O(n)
    Delete          | O(log n)  | O(n)
    """

# ============================================
# 5. INTERVIEW PATTERNS AND TIPS
# ============================================

class InterviewPatterns:
    """
    Common interview patterns and their complexity
    """
    
    @staticmethod
    def pattern_recognition():
        """
        How to identify complexity in interviews:
        
        1. Single loop through n = O(n)
        2. Nested loops = O(n²)
        3. Divide and conquer = O(log n) or O(n log n)
        4. Recursion with branching = O(2^n)
        5. Hash table operations = O(1) average
        
        Interview Question: How would you optimize O(n²) to O(n log n)?
        Answer: Use sorting + two pointers, or use a hash map
        """
        pass
    
    @staticmethod
    def common_optimization_techniques():
        """
        Optimization techniques to reduce complexity:
        
        1. Use hash maps to reduce O(n²) to O(n)
        2. Use two pointers to avoid nested loops
        3. Use prefix sums for range queries
        4. Use binary search to reduce O(n) to O(log n)
        5. Use dynamic programming to avoid recomputation
        """
        pass

# ============================================
# 6. PRACTICE PROBLEMS
# ============================================

class PracticeProblems:
    """
    Interview problems with complexity analysis
    """
    
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        Problem: Find two numbers that sum to target
        O(n) time, O(n) space using hash map
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        """
        Problem: Check if array contains duplicate
        O(n) time, O(n) space using hash set
        """
        return len(nums) != len(set(nums))
    
    @staticmethod
    def max_subarray(nums: List[int]) -> int:
        """
        Problem: Find maximum subarray sum
        O(n) time, O(1) space using Kadane's algorithm
        """
        if not nums:
            return 0
        
        max_ending_here = max_so_far = nums[0]
        
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far

# ============================================
# 7. BENCHMARKING
# ============================================

def benchmark_algorithm(func, *args, **kwargs):
    """
    Measure execution time of an algorithm
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.6f} seconds")
    return result

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("COMPLEXITY ANALYSIS - COMPLETE GUIDE")
    print("=" * 50)
    
    # Test complexity examples
    ca = ComplexityAnalysis()
    
    # O(log n) example
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    binary_search = ca.logarithmic_time_examples()
    result = binary_search(sorted_array, 7)
    print(f"\nBinary Search result: {result} (index of 7)")
    print(f"Time: O(log n), Space: O(1)")
    
    # O(n²) example
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort = ca.quadratic_time_examples()
    sorted_result = bubble_sort(unsorted_array)
    print(f"\nBubble Sort result: {sorted_result}")
    print(f"Time: O(n²), Space: O(1)")
    
    # Test practice problems
    pp = PracticeProblems()
    nums = [2, 7, 11, 15]
    print(f"\nTwo Sum: {pp.two_sum(nums, 9)}")
    print(f"Contains Duplicate: {pp.contains_duplicate([1, 2, 3, 1])}")
    print(f"Max Subarray: {pp.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")
    
    print("\n" + "=" * 50)
    print("KEY INTERVIEW TAKEAWAYS:")
    print("1. Always mention time and space complexity")
    print("2. Explain why your solution has that complexity")
    print("3. Discuss trade-offs between time and space")
    print("4. Consider edge cases and their complexity")
    print("=" * 50)