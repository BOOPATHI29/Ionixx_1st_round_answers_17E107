"""

Find the logic and replicate it .
2 -> 8
3 -> 36
4 -> 272
Sample Output (Need to get input from the user)
Enter the number : 2
Output : 8
Enter the number : 3
Output : 36
Enter the number : 5
Output : ? --> 3150                 """


n=int(input()) # input
 # logic = n power n + n power 2 ( n^3 +n^2 )
print(n**n+n**2) # printing sum
