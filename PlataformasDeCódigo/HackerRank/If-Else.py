"""Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird."""

if __name__ == "__main__":
    n = int(input().strip())
    print("Weird" if (n % 2 == 1) or (6 <= n <= 20) else "Not Weird")
