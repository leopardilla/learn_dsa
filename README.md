# learn_dsa
learn DSA in public
Basic Data Structures
1.	Linear DS
1.1.	Static:
1.1.1.	Array/List
1.2.	Dinamic:
1.1.1.	Stack
1.1.2.	Queue
1.1.3.	Linked list
2.	Non-Linear DS
2.1.	Tree
2.1.1.	Binary tree
2.2.	Graph
3.	Heap
4.	Hash table
5.	Matrix

Operations in data structures:
1.	 traversing - visiting each element of the DS only once
2.	 sorting - sorting the elements in the DS in ascending (from low to high) and descending (from high to low) order
3.	 deleting - removing an element from a DS
4.	 merging - the storage of elements located in two different data files by combining them into one data file
5.	 inserting - addding elements of the same type in a DS
6.	 searching - finding an element in a DS that satisfies one or more conditions

Basic Search and Sort algorithms:
1.	Search
1.1.	Linear Search
1.2.	Binary Search
1.3.	Search an element in a sorted and rotated array
2.	Sort
2.1.	Quick Sort
2.2.	Bubble Sort
2.3.	Selection Sort
2.4.	Insertion Sort
2.5.	Merge Sort
2.6.	Heap Sort (Binary Heap)
2.7.	Topological Sort
2.8.	Etc. (Bucket Sort, Radix Sort, Tim Sort, Shell Sort)
3.	String Search algorithms:
3.1.	 basics
3.2.	 string
3.3.	 string reverse
3.4.	 palindrome sub-string
3.5.	 prefix
3.6.	 suffix
3.7.	 border anagram searching for pattern
3.8.	 naive "compare each char of pattern (P) to each char of text (T)"

Big-O Notation 
Recursion
![image](https://user-images.githubusercontent.com/84455218/134950401-b37c8d51-e251-4200-a259-9e4922baf308.png)

---

# Algorithms >!

### Definitions>!
- [ ] **algorithm** -  a set of instructions for accomplishing a task (instructions are followed step by step to solve problem or to do smth useful). It has an ***input*** which goes through the ***series of computations***, and finally produces an ***output***.

- [ ] **big O notation** - time complexity analysis (the running time of an algorithm) 

- [ ] **recursion** - a common technique for designing algorithms 

- [ ] **Searching algorithms**:
  - [ ] **simple (linear) search algorithm 
  - [ ] **binary search algorithm
  - [ ] upper bound algorithm
  - [ ] lower bound algorithm
  - [ ] sequential search algorithm
  - [ ] depth/ breadth first search

- [ ] logarithm




- [ ] graph algorithm
- [ ] AI algorithm

- [ ] **Sorting algorithms**:
  - [ ] SBI (selection, bubble, insertion)
  - [ ] **merge sort algorithm
  - [ ] **heap sort algorithm
  - [ ] **quicksort algorithm
  - [ ] bucket sort
  - [ ] counting sort

- [ ]  **String Search algorithms**:
- [ ]  ***basics***
  - [ ]  string
  - [ ]  string reverse
  - [ ]  palindrome sub-string
  - [ ]  prefix
  - [ ]  suffix
  - [ ]  border anagram searching for pattern
  - [ ]  naive "compare each char of pattern (P) to each char of text (T)"
- [ ]  ***and***
- [ ]  KMP
- [ ]  Boyer Moore
- [ ]  suffixarray


- [ ] greedy algorithm
- [ ] graph algorithm - a way to model a network: a social network, or a network of roads, or neurons, or any other set of connections
- [ ] breadth-first search
- [ ] Dijkstra’s algorithm 
- [ ] machine-learning algorithm
- [ ] K-nearest neighbors (KNN)
- [ ] specific algorithms for AI, databases etc.

## Search algorithms: simple search, binary search 
**Binary search** is an algorithm; 
its input is a sorted list of elements
If an element you’re looking for is in that list, binary search returns the position where it’s located. 
Otherwise, binary search returns null.

#### *Example:*
**Simple search algorithm.** 
- You have to try to guess my number in the fewest tries possible. With every guess, I’ll tell you if your guess is too low, too high, or correct. 
**Simple search algorithm.** You start guessing like this: 1, 2, 3, 4 ….
**Binary searchalgorithm.** You guess the middle number and eliminate half the emaining numbers every time. Start with 50. Too low, but you just eliminated half the numbers! Now you know that 1–50 are all too low. Next guess: 75. Too high. Next is 63 (halfway between 50 and 75).

*Compare:*  The dictionary has 240,000 words. In the worst case, how many steps do you think each search will take? Simple search could take 240,000 steps if the word you’re looking for is the very last one in the book. With each step of binary search, you cut the number of words in half until you’re left with only one word.

**for any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search will take n steps.**

**NB** 
**Logarithm**. log10 100 is like asking, “How many 10s do we multiply together to get 100?” The answer is 2: 10 × 10. So log10 100 = 2. 
Logs are the flip of exponentials.


##  Time complexity analysis (Big O notation)
Analyze the speed of an algorithm 

## Recursion

## Quicksort

## Greedy algorithm

## Graph algorithms: breadth-first search, Dijkstra’s algorithm 
Breadth-first search and Dijkstra’s algorithm are ways to find the shortest distance between two points in a network: you can use this approach to calculate the degrees of separation between two people or the shortest route to a destination.

## Machine-learning algorithm: K-nearest neighbors (KNN)
You can use KNN to build a recommendations system, an OCR engine, a system to predict stock values—anything that involves predicting a value (“We think Adit will rate this movie 4 stars”) or classifying an object (“That letter is a Q”)

---

# Data structures>!
### Definitions>!
- [ ] **array
- [ ] **linked list
- [ ] hash table
- [ ] **stack
- [ ] **queue
- [ ] matrix
- [ ] spart matrix
- [ ] **heap


- [ ] **graph theory**
  - [ ] graph
  - [ ] **binary tree (max 2 nodes)
  - [ ] binary search tree
  - [ ] BFS
  - [ ] DFS
  - [ ] pre-order (node, left, then right)
  - [ ] in-order (left, node, then right)
  - [ ] trees
  - [ ] hash


- [ ] **operations in data structures**:
  - [ ] traversing - visiting each element of the DS only once
  - [ ] sorting - sorting the elements in the DS in ascending (from low to high) and descending (from high to low) order
  - [ ] deleting - removing an element from a DS 
  - [ ] merging - the storage of elements located in two different data files by combining them into one data file
  - [ ] inserting - addding elements of the same type in a DS 
  - [ ] ***searching*** - finding an element in a DS that satisfies one or more conditions:
    - [ ] linear search
    - [ ] binary search
- [ ] 
- 



## Arrays 
## Linked lists
## Hash tables



### Books:>!
- [Grokking algorithms. An illustrated guide for programmers and other curious people. Aditya Y. Bhargava](https://www.manning.com/books/grokking-algorithms) and [GitHub](https://github.com/egonschiele/grokking_algorithms)
- 
-  
