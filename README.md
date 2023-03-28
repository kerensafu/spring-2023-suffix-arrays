# spring-2023-suffix-arrays
 Assignment 4 for String Algorithms

 Part 1. Pattern search
 We are solving the same problem of searching for pattern P of length M in text T of length N. Implement a pattern search algorithm which uses the suffix array of T that works in time O(M log n).

 You can use any implementation of the suffix array construction algorithm in the language of your choice. Some implementations can be found here:
 https://www.geeksforgeeks.org/suffix-array-set-1-introduction/

 However, if you want this assignment to be somewhat useful for your future projects, you should implement the search in c, and use one of the fastest suffix array construction algorithms - the qsufsort by Larsson. The code of the original algorithm is here.

 After you implement the pattern search, please make sure that your algorithm correctly finds all occurrences of the pattern by running the stress test (see Assignment A1).

 Part 2. Counting occurrences
 In this part you need to use the suffix array of T to count the total number of occurrences of a given pattern P in text T. Implement and run stress tests to make sure your algorithm works correctly. Make sure that your algorithm runs in time O(M log N), even if the pattern occurs O(N) times.

 Submit all your code in a single zipped file. This should include the suffix array construction code (with references to the source), your own code for the pattern search and for the pattern counting, and both stress tests.

 At the end of this document (or in a separate README file), explain how to run your code (including the construction of the suffix array) and how to run stress tests.

HOW TO RUN CODE:
when running pattern_search.py, it takes in two strings from the command line. The first string is the text that you are searching, and the second string as the pattern that you are searching for.

HOW TO RUN STRESS TEST:
