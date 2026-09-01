# Data Structures and Algorithms From Scratch 

A complete hands-on exploration of Data Structures and Algorithms using Python, starting from fundamental programming concepts and complexity analysis and progressing toward advanced data structures, algorithms, optimization techniques, and algorithm engineering.

This repository is focused on understanding how algorithms actually work.

I will implement important data structures and algorithms from scratch, study their internal behavior, analyze time and space complexity, compare different approaches, benchmark implementations, and understand where each technique is useful.

The goal is to build a strong foundation in algorithmic thinking and develop the ability to reason about performance, scalability, memory usage, and computational tradeoffs.

---

# Why Data Structures and Algorithms?

Software systems constantly need to store, access, search, transform, organize, and process data.

The choice of data structure and algorithm can directly affect:

```text
Performance
Memory Usage
Latency
Throughput
Scalability
Implementation Complexity
```

For example, a problem that requires:

```text
O(n²)
```

with one approach may be reduced to:

```text
O(n log n)
```

or:

```text
O(n)
```

with a different data structure or algorithm.

This repository focuses on understanding why those differences occur and how to make better algorithmic decisions.

---

# Complete Learning Flow

```text
Programming Fundamentals
          ↓
Complexity Analysis
          ↓
Arrays
          ↓
Strings
          ↓
Hashing
          ↓
Linked Lists
          ↓
Stacks and Queues
          ↓
Recursion
          ↓
Searching
          ↓
Sorting
          ↓
Divide and Conquer
          ↓
Trees
          ↓
Binary Search Trees
          ↓
Balanced Trees
          ↓
Heaps and Priority Queues
          ↓
Tries
          ↓
Graphs
          ↓
Graph Traversal
          ↓
Shortest Paths
          ↓
Minimum Spanning Trees
          ↓
Disjoint Set Union
          ↓
Greedy Algorithms
          ↓
Backtracking
          ↓
Dynamic Programming
          ↓
Bit Manipulation
          ↓
Advanced Data Structures
          ↓
Advanced Graph Algorithms
          ↓
Advanced String Algorithms
          ↓
Computational Geometry
          ↓
Randomized Algorithms
          ↓
Optimization and Algorithm Engineering
```

---

# 1. Foundations

The repository begins with the fundamentals required to understand and implement algorithms effectively.

Topics include:

```text
Variables
Data Types
Functions
Loops
Conditionals
References
Mutable and Immutable Objects
Memory Concepts
Input and Output
Recursion
```

I will also explore how Python's object model and memory behavior affect algorithm implementation.

---

# 2. Complexity Analysis

Complexity analysis is used throughout the repository to understand how an algorithm behaves as the input grows.

Topics include:

```text
Time Complexity
Space Complexity
Best Case
Average Case
Worst Case
Amortized Analysis
```

Common complexity classes:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
```

The focus is not simply memorizing Big-O notation, but understanding where the complexity comes from.

---

# 3. Arrays

Arrays are one of the fundamental building blocks of algorithm design.

Topics include:

```text
Static Arrays
Dynamic Arrays
Traversal
Insertion
Deletion
Searching
Updating
Prefix Sums
Difference Arrays
In-place Operations
```

I will also investigate how Python lists behave internally and compare them with a custom dynamic array implementation.

---

# 4. Array Techniques

Important array techniques include:

```text
Two Pointers
Sliding Window
Prefix Sum
Difference Array
Partitioning
Frequency Counting
In-place Processing
Kadane's Algorithm
```

General approach:

```text
Input
  ↓
Understand Structure
  ↓
Choose Technique
  ↓
Reduce Unnecessary Work
  ↓
Process Data
  ↓
Result
```

---

# 5. Strings

Strings are fundamental to text processing and many algorithmic problems.

Topics include:

```text
String Traversal
Character Frequency
String Comparison
Palindrome
Anagrams
Substrings
Subsequences
String Rotation
Pattern Matching
```

The repository will progress from simple string operations to advanced string algorithms.

---

# 6. Hashing

Hashing provides efficient mechanisms for lookup and association.

Topics include:

```text
Hash Functions
Hash Tables
Hash Maps
Hash Sets
Collision Handling
Chaining
Open Addressing
Load Factor
Resizing
```

I will implement a hash table from scratch to understand what happens internally when keys are inserted, searched, updated, and removed.

---

# 7. Linked Lists

I will implement:

```text
Singly Linked List
Doubly Linked List
Circular Linked List
```

Operations include:

```text
Insertion
Deletion
Traversal
Search
Reverse
Middle Element
Cycle Detection
Merge
```

Important techniques include:

```text
Fast and Slow Pointers
Pointer Manipulation
In-place Reversal
```

---

# 8. Stacks

A stack follows the:

```text
LIFO
Last In, First Out
```

principle.

Implementations:

```text
Array-based Stack
Linked-list Stack
```

Applications include:

```text
Expression Evaluation
Parentheses Matching
Function Calls
Recursion
Undo Operations
Monotonic Stack
```

---

# 9. Queues

A queue follows the:

```text
FIFO
First In, First Out
```

principle.

Implementations include:

```text
Queue
Circular Queue
Deque
Priority Queue
```

Applications include:

```text
Scheduling
Buffering
Breadth-First Search
Task Processing
Event Processing
```

---

# 10. Recursion

Recursion is a fundamental technique behind many tree, graph, divide-and-conquer, and backtracking algorithms.

Topics include:

```text
Base Case
Recursive Case
Call Stack
Recursive Tree
Tail Recursion
Memoization
Recursion Depth
```

I will trace recursive execution to understand how function calls are created and removed from the call stack.

---

# 11. Searching

Searching algorithms will progress from basic to more advanced techniques.

```text
Linear Search
Binary Search
Jump Search
Interpolation Search
```

Binary search variations:

```text
First Occurrence
Last Occurrence
Lower Bound
Upper Bound
Search on Answer
Rotated Sorted Array
```

The repository will focus on understanding why binary search reduces the search space and how the same idea can be applied beyond sorted arrays.

---

# 12. Sorting

Sorting algorithms will be implemented and compared.

### Basic Sorting

```text
Bubble Sort
Selection Sort
Insertion Sort
```

### Efficient Sorting

```text
Merge Sort
Quick Sort
Heap Sort
```

### Non-comparison Sorting

```text
Counting Sort
Radix Sort
Bucket Sort
```

Each implementation will examine:

```text
Time Complexity
Space Complexity
Stability
In-place Behavior
Best Use Case
Limitations
```

---

# 13. Divide and Conquer

Divide and conquer breaks a large problem into smaller subproblems.

```text
Problem
   ↓
Divide
   ↓
Solve Subproblems
   ↓
Combine
   ↓
Result
```

Algorithms include:

```text
Merge Sort
Quick Sort
Binary Search
Closest Pair
Large Number Multiplication
```

---

# 14. Trees

Trees represent hierarchical relationships.

Core concepts:

```text
Root
Node
Edge
Parent
Child
Leaf
Depth
Height
Subtree
```

Tree traversals:

```text
Preorder
Inorder
Postorder
Level Order
```

---

# 15. Binary Trees

A binary tree contains at most two children per node.

Topics include:

```text
Binary Tree Construction
Insertion
Deletion
Traversal
Height
Depth
Diameter
Balanced Tree Checking
Lowest Common Ancestor
```

---

# 16. Binary Search Trees

A Binary Search Tree maintains an ordering relationship between nodes.

```text
        Root
       /    \
  Smaller  Larger
```

Topics include:

```text
Search
Insertion
Deletion
Minimum
Maximum
Successor
Predecessor
```

I will also explore how tree balance affects performance.

---

# 17. Balanced Trees

Advanced search trees include:

```text
AVL Tree
Red-Black Tree
```

Topics include:

```text
Balance Factors
Rotations
Rebalancing
Insertion
Deletion
Height
```

The goal is to understand how balanced trees maintain efficient operations.

---

# 18. Heaps

A heap provides efficient access to the minimum or maximum element.

I will implement:

```text
Min Heap
Max Heap
Heapify
Build Heap
Insert
Delete
Extract Min
Extract Max
```

Applications include:

```text
Priority Queues
Scheduling
Top-K Processing
Heap Sort
Graph Algorithms
```

---

# 19. Priority Queues

Priority queues process elements according to priority rather than insertion order.

```text
Element
   ↓
Priority
   ↓
Priority Queue
   ↓
Highest / Lowest Priority
   ↓
Processed
```

Applications include:

```text
Scheduling
Dijkstra's Algorithm
Event Processing
Task Management
```

---

# 20. Tries

A Trie is a tree-based structure designed for strings and prefix operations.

```text
Words
  ↓
Trie
  ↓
Character Paths
  ↓
Prefix Search
```

Operations include:

```text
Insert
Search
Delete
Prefix Search
Autocomplete
```

---

# 21. Graphs

Graphs represent relationships between entities.

I will explore:

```text
Vertices
Edges
Directed Graphs
Undirected Graphs
Weighted Graphs
Unweighted Graphs
Cyclic Graphs
Acyclic Graphs
```

Graph representations:

```text
Adjacency Matrix
Adjacency List
Edge List
```

---

# 22. Breadth-First Search

BFS explores a graph level by level.

```text
Start Node
    ↓
Queue
    ↓
Neighbors
    ↓
Next Level
    ↓
Continue
```

Applications include:

```text
Shortest Path in Unweighted Graphs
Level Traversal
Connected Components
State Exploration
```

---

# 23. Depth-First Search

DFS explores a path deeply before backtracking.

```text
Start
  ↓
Neighbor
  ↓
Deeper Neighbor
  ↓
Deepest Node
  ↓
Backtrack
```

Applications include:

```text
Cycle Detection
Connected Components
Path Finding
Topological Sorting
Graph Analysis
```

---

# 24. Topological Sorting

Topological sorting is used to order dependencies in a Directed Acyclic Graph.

```text
Dependency
     ↓
Prerequisite
     ↓
Task
```

Implementations:

```text
Kahn's Algorithm
DFS-based Topological Sort
```

Applications include:

```text
Task Dependencies
Build Systems
Package Dependencies
Workflow Processing
```

---

# 25. Shortest Path Algorithms

I will implement and compare:

```text
BFS
Dijkstra
Bellman-Ford
Floyd-Warshall
A*
```

The focus will be on understanding when each algorithm should be used and what assumptions each algorithm makes.

---

# 26. Minimum Spanning Trees

I will explore:

```text
Kruskal's Algorithm
Prim's Algorithm
```

Topics include:

```text
Edge Selection
Cycle Prevention
Disjoint Sets
Minimum Cost Connectivity
```

---

# 27. Disjoint Set Union

Disjoint Set Union, also known as Union-Find, maintains collections of connected components.

Operations:

```text
Find
Union
```

Optimizations:

```text
Path Compression
Union by Rank
Union by Size
```

Applications include:

```text
Connected Components
Cycle Detection
Kruskal's Algorithm
Network Connectivity
```

---

# 28. Greedy Algorithms

Greedy algorithms make a locally optimal decision at each step.

```text
Current State
     ↓
Best Local Choice
     ↓
Update State
     ↓
Repeat
```

Topics include:

```text
Activity Selection
Fractional Knapsack
Interval Scheduling
Huffman Coding
Minimum Spanning Trees
```

I will also study cases where greedy decisions do not produce an optimal solution.

---

# 29. Backtracking

Backtracking explores possible choices and reverses decisions when a path cannot produce a valid result.

```text
Choose
  ↓
Explore
  ↓
Valid?
 ├── Yes → Continue
 └── No  → Backtrack
```

Topics include:

```text
Permutations
Combinations
Subsets
N-Queens
Sudoku
Maze Problems
Constraint Problems
```

---

# 30. Dynamic Programming

Dynamic Programming is used when a problem contains overlapping subproblems and useful optimal substructure.

Two major approaches:

```text
Top-Down
    ↓
Memoization
```

and:

```text
Bottom-Up
    ↓
Tabulation
```

Topics include:

```text
1D DP
2D DP
Grid DP
Sequence DP
Knapsack
Subsequence Problems
Interval DP
Tree DP
Bitmask DP
Digit DP
```

The focus will be on designing the state and transition rather than memorizing solutions.

---

# 31. Knapsack and Optimization Problems

I will implement:

```text
0/1 Knapsack
Unbounded Knapsack
Bounded Knapsack
Subset Sum
Partition
Coin Change
```

Each implementation will explore the relationship between:

```text
State
Transition
Base Case
Optimization
```

---

# 32. Advanced String Algorithms

The repository will progress from basic pattern matching to advanced string processing.

```text
Naive Pattern Matching
KMP
Rabin-Karp
Z Algorithm
```

Advanced structures:

```text
Trie
Suffix Array
Suffix Tree
```

---

# 33. Bit Manipulation

Bit manipulation provides efficient ways to represent and process binary states.

Topics include:

```text
AND
OR
XOR
NOT
Left Shift
Right Shift
Bit Masks
Set Bit
Clear Bit
Toggle Bit
Count Bits
Power of Two
```

Applications include:

```text
Subset Representation
State Compression
Bitmask DP
Low-level Optimization
```

---

# 34. Mathematical Algorithms

Algorithmic mathematics includes:

```text
GCD
LCM
Euclidean Algorithm
Prime Numbers
Sieve of Eratosthenes
Prime Factorization
Modular Arithmetic
Fast Exponentiation
Combinatorics
```

These concepts will also be connected to other algorithms where appropriate.

---

# 35. Advanced Graph Algorithms

Advanced graph topics include:

```text
Strongly Connected Components
Kosaraju's Algorithm
Tarjan's Algorithm
Bridges
Articulation Points
Eulerian Path
Eulerian Circuit
Bipartite Graphs
Network Flow
Maximum Flow
```

---

# 36. Network Flow

I will explore flow networks using:

```text
Source
  ↓
Network
  ↓
Capacity
  ↓
Sink
```

Algorithms include:

```text
Ford-Fulkerson
Edmonds-Karp
Dinic
```

The focus will be on understanding how flow is routed through a network and how capacity constraints affect the solution.

---

# 37. Advanced Data Structures

Advanced structures include:

```text
Segment Tree
Fenwick Tree
Sparse Table
Disjoint Set Union
Interval Tree
Binary Lifting
```

These structures will be studied through their supported operations, complexity, and practical use cases.

---

# 38. Segment Trees

Segment trees support efficient range queries and updates.

```text
Array
  ↓
Segment Tree
  ↓
Range Query
  +
Point / Range Update
```

Topics include:

```text
Range Sum
Range Minimum
Range Maximum
Lazy Propagation
```

---

# 39. Fenwick Trees

Fenwick Trees provide efficient prefix aggregation.

```text
Update
  ↓
Fenwick Tree
  ↓
Prefix Query
```

I will compare Fenwick Trees with Segment Trees to understand when each structure is more appropriate.

---

# 40. Sparse Tables

Sparse Tables are useful for efficient queries over static data.

Topics include:

```text
Preprocessing
Range Minimum Query
Idempotent Operations
Binary Lifting
```

---

# 41. Binary Lifting

Binary lifting allows efficient ancestor and jump queries.

Applications include:

```text
Lowest Common Ancestor
Ancestor Queries
Tree Queries
Functional Graphs
```

---

# 42. Advanced Dynamic Programming

Advanced DP techniques include:

```text
State Compression
Bitmask DP
Digit DP
Tree DP
Interval DP
Probability DP
Optimization DP
```

The focus will be on understanding how complex states can be represented efficiently.

---

# 43. Computational Geometry

I will explore fundamental computational geometry concepts.

```text
Points
Lines
Segments
Orientation
Cross Product
Distance
Line Intersection
Convex Hull
Closest Pair
```

Algorithms include:

```text
Graham Scan
Monotonic Chain
```

---

# 44. Randomized Algorithms

I will explore algorithms that use controlled randomness.

```text
Randomized QuickSort
Randomized Selection
Reservoir Sampling
Randomized Hashing
```

The goal is to understand expected complexity, randomness, and why randomized approaches can be useful.

---

# 45. Amortized Analysis

Some operations may occasionally be expensive while remaining efficient across a sequence of operations.

I will study:

```text
Dynamic Arrays
Stack Operations
Queue Operations
Union-Find
```

Analysis techniques include:

```text
Aggregate Method
Accounting Method
Potential Method
```

---

# 46. Algorithm Design Techniques

The repository will organize algorithms around their underlying design strategies.

```text
Brute Force
Two Pointers
Sliding Window
Prefix Sum
Binary Search
Divide and Conquer
Greedy
Backtracking
Dynamic Programming
Randomization
State Compression
```

The objective is to understand how a problem can be transformed into a more efficient computational process.

---

# 47. Problem-Solving Workflow

For each significant problem, I will follow a structured process.

```text
Understand the Problem
        ↓
Identify Inputs and Outputs
        ↓
Analyze Constraints
        ↓
Build a Simple Solution
        ↓
Identify the Bottleneck
        ↓
Choose the Data Structure
        ↓
Choose the Algorithm
        ↓
Analyze Complexity
        ↓
Implement
        ↓
Test
        ↓
Benchmark
        ↓
Optimize
```

---

# 48. From Simple to Optimized

Important problems will be explored through multiple approaches.

```text
Brute Force
     ↓
Improved Approach
     ↓
Efficient Approach
     ↓
Optimized Approach
```

For each approach, I will document:

```text
Idea
Implementation
Time Complexity
Space Complexity
Advantages
Limitations
Tradeoffs
```

---

# 49. Complexity and Performance

Major algorithms will be compared using both theoretical and practical measurements.

Example:

```text
Algorithm          Time           Space

Linear Search      O(n)           O(1)
Binary Search      O(log n)       O(1)
Merge Sort         O(n log n)     O(n)
Quick Sort         O(n log n)*    O(log n)*
Heap Sort          O(n log n)     O(1)
```

The repository will distinguish between:

```text
Theoretical Complexity
        ↓
Actual Runtime
```

because real performance is also affected by:

```text
Hardware
Memory Access
Cache Behavior
Language Implementation
Constant Factors
Input Distribution
```

---

# 50. Testing

Data structures and algorithms will be tested against different types of input.

```text
Normal Cases
Boundary Cases
Empty Input
Single Element
Duplicate Values
Large Input
Invalid Input
Worst-Case Input
Randomized Input
```

The objective is to verify both correctness and robustness.

---

# 51. Benchmarking

Where useful, implementations will be benchmarked against different input sizes.

Measurements may include:

```text
Execution Time
Memory Usage
Input Size
Operation Count
Throughput
```

This provides a practical comparison between different algorithms and implementations.

---

# 52. Visualization

Some algorithms are easier to understand visually.

Where useful, I will create visualizations for:

```text
Sorting
Trees
Graphs
Recursion
Dynamic Programming
Heaps
Binary Search
Path Finding
```

The purpose is to make algorithm state and execution easier to understand.

---

# 53. Python Implementations

Python is the primary implementation language.

I will use Python's built-in data structures where appropriate, while also implementing important structures manually.

Examples:

```text
Python list
     vs
Custom Dynamic Array
```

```text
Python dict
     vs
Custom Hash Table
```

```text
heapq
     vs
Custom Heap
```

This creates a distinction between:

```text
Using a Data Structure
        ↓
Understanding a Data Structure
```

---

# Repository Structure

```text
data-structures-and-algorithms-from-scratch/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
│
├── 01_foundations/
│   ├── complexity/
│   ├── recursion/
│   ├── memory/
│   └── mathematics/
│
├── 02_arrays/
│   ├── basics/
│   ├── two_pointers/
│   ├── sliding_window/
│   ├── prefix_sum/
│   ├── difference_array/
│   └── advanced/
│
├── 03_strings/
│   ├── basics/
│   ├── frequency/
│   ├── palindrome/
│   ├── substring/
│   └── pattern_matching/
│
├── 04_hashing/
│   ├── hash_table/
│   ├── hash_map/
│   ├── hash_set/
│   └── collision_handling/
│
├── 05_linked_lists/
│   ├── singly/
│   ├── doubly/
│   ├── circular/
│   └── techniques/
│
├── 06_stacks_queues/
│   ├── stack/
│   ├── queue/
│   ├── deque/
│   └── priority_queue/
│
├── 07_searching/
│   ├── linear_search/
│   ├── binary_search/
│   ├── search_on_answer/
│   └── advanced/
│
├── 08_sorting/
│   ├── bubble_sort/
│   ├── selection_sort/
│   ├── insertion_sort/
│   ├── merge_sort/
│   ├── quick_sort/
│   ├── heap_sort/
│   └── non_comparison/
│
├── 09_trees/
│   ├── binary_tree/
│   ├── bst/
│   ├── avl/
│   ├── red_black_tree/
│   ├── heap/
│   └── traversals/
│
├── 10_tries/
│   ├── trie/
│   ├── autocomplete/
│   └── prefix_search/
│
├── 11_graphs/
│   ├── representations/
│   ├── bfs/
│   ├── dfs/
│   ├── topological_sort/
│   ├── shortest_path/
│   ├── mst/
│   ├── dsu/
│   ├── scc/
│   ├── bridges/
│   └── network_flow/
│
├── 12_greedy/
│   ├── scheduling/
│   ├── intervals/
│   ├── knapsack/
│   └── huffman/
│
├── 13_backtracking/
│   ├── permutations/
│   ├── combinations/
│   ├── n_queens/
│   ├── sudoku/
│   └── maze/
│
├── 14_dynamic_programming/
│   ├── 1d/
│   ├── 2d/
│   ├── knapsack/
│   ├── subsequence/
│   ├── interval_dp/
│   ├── tree_dp/
│   ├── bitmask_dp/
│   └── digit_dp/
│
├── 15_bit_manipulation/
│   ├── operations/
│   ├── bit_masks/
│   └── bitmask_dp/
│
├── 16_mathematics/
│   ├── gcd_lcm/
│   ├── primes/
│   ├── modular_arithmetic/
│   ├── combinatorics/
│   └── fast_power/
│
├── 17_range_queries/
│   ├── segment_tree/
│   ├── fenwick_tree/
│   ├── sparse_table/
│   └── lazy_propagation/
│
├── 18_string_algorithms/
│   ├── kmp/
│   ├── rabin_karp/
│   ├── z_algorithm/
│   ├── suffix_array/
│   └── suffix_tree/
│
├── 19_computational_geometry/
│   ├── orientation/
│   ├── intersections/
│   ├── convex_hull/
│   └── closest_pair/
│
├── 20_randomized_algorithms/
│   ├── randomized_quicksort/
│   ├── randomized_selection/
│   ├── reservoir_sampling/
│   └── randomized_hashing/
│
├── 21_algorithm_design/
│   ├── brute_force/
│   ├── divide_and_conquer/
│   ├── greedy/
│   ├── backtracking/
│   ├── dynamic_programming/
│   └── randomization/
│
├── src/
│   └── dsa/
│       ├── arrays/
│       ├── strings/
│       ├── hashing/
│       ├── linked_lists/
│       ├── stacks/
│       ├── queues/
│       ├── trees/
│       ├── heaps/
│       ├── tries/
│       ├── graphs/
│       ├── dp/
│       └── algorithms/
│
├── notebooks/
├── benchmarks/
├── visualizations/
├── experiments/
└── tests/
```

---

# Learning Progression

The repository progresses through four major stages.

## Stage 1: Foundations

```text
Programming Fundamentals
Complexity Analysis
Arrays
Strings
Hashing
Linked Lists
Stacks
Queues
Recursion
Searching
Sorting
```

## Stage 2: Core Data Structures

```text
Trees
Binary Search Trees
Balanced Trees
Heaps
Priority Queues
Tries
Graphs
Disjoint Set Union
```

## Stage 3: Core Algorithms

```text
BFS
DFS
Topological Sorting
Shortest Paths
Minimum Spanning Trees
Greedy Algorithms
Backtracking
Dynamic Programming
Bit Manipulation
```

## Stage 4: Advanced Algorithms and Structures

```text
Segment Trees
Fenwick Trees
Sparse Tables
Binary Lifting
Advanced Graph Algorithms
Advanced String Algorithms
Network Flow
Computational Geometry
Randomized Algorithms
Advanced Dynamic Programming
Algorithm Engineering
```

---

# What I Want to Understand

For every important data structure and algorithm, I want to understand:

```text
What problem does it solve?

How does it work internally?

Why does it work?

What data structure does it require?

What are its time and space complexities?

What are its limitations?

What alternatives exist?

When is one approach better than another?

What happens with large inputs?

Can the implementation be optimized?

What are the practical tradeoffs?
```

---

# Final Goal

The purpose of this repository is not to collect isolated implementations.

The goal is to develop a deeper understanding of how data structures organize information and how algorithms transform that information efficiently.

The complete workflow is:

```text
Understand the Problem
        ↓
Understand the Data
        ↓
Choose the Data Structure
        ↓
Choose the Algorithm
        ↓
Implement From Scratch
        ↓
Analyze Complexity
        ↓
Test Correctness
        ↓
Benchmark Performance
        ↓
Identify Bottlenecks
        ↓
Optimize
        ↓
Understand the Tradeoffs
```

This repository represents my complete exploration of Data Structures and Algorithms using Python, progressing from fundamental concepts to advanced data structures, algorithms, optimization techniques, and practical algorithm engineering.
