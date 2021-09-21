# learn_dsa
learn DSA in public


# Algorithms

### Definitions
- [ ] **algorithm** -  a set of instructions for accomplishing a task (instructions are followed step by step to solve problem or to do smth useful). It has an ***input*** which goes through the ***series of computations***, and finally produces an ***output***.
- [ ] **Searching algorithms**:
- [ ] simple (linear) search algorithm 
- [ ] binary search algorithm
- [ ] upper bound algorithm
- [ ] lower bound algorithm
- [ ] sequential search algorithm

- [ ] logarithm


- [ ] **big O notation** - time complexity analysis (the running time of an algorithm) 


- [ ] **recursion** - a common technique for designing algorithms 


- [ ] graph algorithm
- [ ] AI algorithm

- [ ] **Sorting algorithms**:
- [ ] SBI (selection, bubble, insertion)
- [ ] merger sort algorithm
- [ ] heap sort algorithm
- [ ] quicksort algorithm

- [ ]  **String Search algorithms**:
- [ ]  ***basics***
- [ ]  string
- [ ]  string reverse
- [ ]  palindrome sub-string
- [ ]  prefix, suffix
- [ ]  border anagram searching for pattern
- [ ]  naive "compare each char of pattern (P) to each char of text (T)"


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

# Data structures
### Definitions
- [ ] array
- [ ] linked list
- [ ] hash tables
- [ ] trees
- [ ] stacks
- [ ] queues
- [ ] graph
- [ ] hash

## Arrays 
## Linked lists
## Hash tables



### Books:
- [Grokking algorithms. An illustrated guide for programmers and other curious people. Aditya Y. Bhargava](https://www.manning.com/books/grokking-algorithms) and [GitHub](https://github.com/egonschiele/grokking_algorithms)
- 
-  
