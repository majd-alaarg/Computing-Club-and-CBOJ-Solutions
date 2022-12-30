#PROBLEM START

#Given a string S, please determine whether or not S is a palindrome. A palindrome is a sequence of letters that is the same when read forwards or backwards.

#Input Specification
#The first and only line will contain a string S consisting of lowercase letters in the English alphabet. The length of S will not exceed 105 letters (1≤|S|≤105).

#Output Specification
#On a single line output YES if the string is a palindrome, and NO otherwise.


#PROBLEM END

n = input()
if str(n) == str(n)[::-1]:
  print("YES")
else:
  print("NO")