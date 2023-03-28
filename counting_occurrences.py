import sys
import pattern_search.py

#In this part you need to use the suffix array of T to count the total number of occurrences of a given pattern P in text T.
#Implement and run stress tests to make sure your algorithm works correctly.
#Make sure that your algorithm runs in time O(M log N), even if the pattern occurs O(N) times.

# finds all iterations of a pattern in a string, not just the first one
# binary search taken from geeksforgeeks
def better_search(pat, txt, suffArr, n):
    arr = []


    m = len(pat)
    l = 0
    r = n-1
    while l <= r:
        mid = l + (r - l)//2
        res = txt[suffArr[mid]:suffArr[mid]+m]
        if res == pat:
            print("Pattern found at index", suffArr[mid])
            #now we want to go down the rest of the suffix array and get all the ones that startw that suffix
            return suffArr[mid]
        if res < pat:
            l = mid + 1
        else:
            r = mid - 1
    print("Pattern not found")






def main():
    txt = sys.argv[1]  # text
    pat = sys.argv[2]   # pattern to be searched in text

    # Build suffix array
    n = len(txt)
    suffArr = pattern_search.buildSuffixArray(txt, n)

    # search pat in txt using the built suffix array
    better_search(pat, txt, suffArr, n)
    return 0

if __name__ == '__main__':
    sys.exit(main())
