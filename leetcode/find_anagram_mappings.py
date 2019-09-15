# https://leetcode.com/problems/find-anagram-mappings/ (Premium)
# https://leetcode.com/problems/find-anagram-mappings/solution/


"""
Find Anagram Mappings
Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example (and Test case 0), given
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return [1, 4, 3, 2, 0]
as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.

Note:
1. A, B have equal lengths in range [1, 100].
2. A[i], B[i] are integers in range [0, 10^5].
"""

# runtime 40 ms, 74%; memory 13.9 MB, 25%
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        a = collections.defaultdict(int)
        res = []
        for i, c in enumerate(B):
            a[c] = i
        for i in range(len(A)):
            res.append(a[A[i]])
        return res


# condensed code from solution
# runtime 40 ms, 74%; memory 13.8 MB, 25%
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        D = {x: i for i, x in enumerate(B)}
        return [D[x] for x in A]


"""
Solution
Approach #1: Hash Table [Accepted]

Intuition
Take the example A = [12, 28, 46], B = [46, 12, 28]. We want to know where the 12 occurs in B, say at position 1; then where the 28 occurs in B, which is position 2; then where the 46 occurs in B, which is position 0.

If we had a dictionary (hash table) D = {46: 0, 12: 1, 28: 2}, then this question could be handled easily.

Algorithm
Create the hash table D as described above. Then, the answer is a list of D[A[i]] for i = 0, 1, ....
[code is above]

Complexity Analysis
- Time Complexity: O(N), where N is the length of A.
- Space Complexity: O(N).
"""
