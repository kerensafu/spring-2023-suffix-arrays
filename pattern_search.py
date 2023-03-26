#We are solving the same problem of searching for pattern P of length M in text T of length N.
#Implement a pattern search algorithm which uses the suffix array of T that works in time O(M log n).

# This file contains an implementation of the algorithm presented in "Faster
#Suffix Sorting" by N. Jesper Larsson (jesper@cs.lth.se) and Kunihiko
# Sadakane (sada@is.s.u-tokyo.ac.jp). It is based off of qsufsort.c, also by N. Jesper Larsson.
def cons_suf_arr(str):
    return "hi"


import sys

# A suffix array based search function to search a given pattern
# 'pat' in given text 'txt' using suffix array suffArr[]
def search(pat, txt, suffArr, n):

    # Get the length of the pattern
    m = len(pat)

    # Initialize left and right indexes
    l = 0
    r = n-1

    # Do simple binary search for the pat in txt using the built suffix array
    while l <= r:

        # Find the middle index of the current subarray
        mid = l + (r - l)//2

        # Get the substring of txt starting from suffArr[mid] and of length m
        res = txt[suffArr[mid]:suffArr[mid]+m]

        # If the substring is equal to the pattern
        if res == pat:

            # Print the index and return
            print("Pattern found at index", suffArr[mid])
            return

        # If the substring is less than the pattern
        if res < pat:

            # Move to the right half of the subarray
            l = mid + 1
        else:

            # Move to the left half of the subarray
            r = mid - 1

    # If the pattern is not found
    print("Pattern not found")

def buildSuffixArray(txt, n):

    # Create a list of all suffixes
    suffixes = [txt[i:] for i in range(n)]

    # Sort the suffixes
    suffixes.sort()

    # Create the suffix array
    suffArr = [txt.index(suffix) for suffix in suffixes]
    return suffArr

class Suffix:
    def __init__(self, index, suff):
        self.index = index
        self.suff = suff

# A comparison function used by sort() to compare two suffixes
def cmp(a, b):
    return (a.suff < b.suff) - (a.suff > b.suff)

# This is the main function that takes a string 'txt' of size n as an
# argument, builds and return the suffix array for the given string
def build_suffix_array(txt, n):
    # A structure to store suffixes and their indexes
    suffixes = [Suffix(i, txt[i:]) for i in range(n)]

    # Sort the suffixes using the comparison function
    # defined above.
    suffixes.sort(key=cmp)

    # Store indexes of all sorted suffixes in the suffix array
    suffix_arr = [suffixes[i].index for i in range(n)]

    # Return the suffix array
    return suffix_arr

# A utility function to print an array of given size
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def naive_search (T, P):
    matches = []
    plen = len(P)
    N = len(T)

    #naive algorithm
    for i in range (N - plen + 1):
        j = 0
        while j < plen and P[j] == T[i+j]:
            j += 1

        if j == plen:
            matches.append(i)

    return matches

# Driver program to test above function
def main():
    txt = "banana"  # text
    pat = "nan"   # pattern to be searched in text

    # Build suffix array
    n = len(txt)
    suffArr = buildSuffixArray(txt, n)

    # search pat in txt using the built suffix array
    search(pat, txt, suffArr, n)
    return 0

if __name__ == '__main__':
    sys.exit(main())

# This code is contributed by Vikram_Shirsat
