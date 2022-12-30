#PROBLEM START

#Given a string S, please determine the longest palindromic substring in S. A palindrome is a sequence of letters that is the same when read forwards or backwards.
#For this problem, Python users are recommended to use PYPY over CPython.

#Input Specification
#The first and only line will contain a string S consisting of lowercase letters in the English alphabet. This time, the length of S will not exceed 10^5 letters (1≤|S|≤10^5).

#Output Specification
#On a single line output an integer indicating the longest palindromic substring's length.

#PROBLEM END


def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def Manachen(string):
    string = UpdatedString(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2*C - i
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass
        
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    
    r, c = max(LPS), LPS.index(max(LPS))
    return r

print(Manachen(input()))
