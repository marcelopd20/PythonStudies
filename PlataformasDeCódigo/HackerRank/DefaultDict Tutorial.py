"""In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .

Expected output:

1 3
-1
Input Format

The first line contains integers,  and  separated by a space.
The next  lines contains the words belonging to group .
The next  lines contains the words belonging to group .

Constraints




Output Format

Output  lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and .
'b' appeared  times in positions  and .
In the sample problem, if 'c' also appeared in word group , you would print ."""
from collections import defaultdict

"""n,m = (int(x) for x in input().split())
d = defaultdict(list)
for x in range(n):
    d['A'].append(input())
for x in range(m):
    d['B'].append(input())
for x in d['B']:
    if x in d['A']:
        for y in range(len(d['A'])):
            if d['A'][y] == x:
                print(y+1, end=' ')
        print()
    else:
        print(-1)
"""

n, m = (int(x) for x in input().split())
d = defaultdict(list)
for a in range(n):
    d[input()].append(a+1)
for a in range(m):
    print(*d[input()] or -1)
